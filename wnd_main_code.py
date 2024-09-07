import json
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from memwin import *
import win32gui
import win32process
import win32api
import win32con
import qdarkstyle

from ui.wnd_main import Ui_WndMain
from utils.string import HexStr
from widgets.botton import AttachButton



class WndMain(QMainWindow, Ui_WndMain):
    sig_hwnd_changed = Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))
        app_path = os.path.join(os.getenv('APPDATA'), 'DC WinHackToolKit')
        os.makedirs(app_path, exist_ok=True)
        self.config_path = os.path.join(app_path, 'config.json')
        self.hwnd_str = ''
        self.init_widgets()
        self.read_config()
        self.init_sig_slots()

    def init_widgets(self):
        self.btn_attach.__class__ = AttachButton
        self.btn_attach.setText('🔍')
        self.btn_attach.setFont(QFont('Segoe UI', 15))
        self.edt_hwnd.selectAll()

    def init_sig_slots(self):
        self.sig_hwnd_changed.connect(self.on_hwnd_changed)
        self.chk_hwnd_hex.stateChanged.connect(self.on_chk_hwnd_hex_changed)
        self.chk_pid_hex.stateChanged.connect(self.on_chk_pid_hex_changed)
        self.chk_tid_hex.stateChanged.connect(self.on_chk_tid_hex_changed)

    def on_hwnd_changed(self, hwnd: int):
        if self.chk_hwnd_hex.isChecked():
            self.hwnd_str = HexStr(hwnd)
            print(f'self.hwnd: {self.hwnd_str}')
        else:
            self.hwnd_str = str(hwnd)
        window_title = win32gui.GetWindowText(hwnd)
        window_class = win32gui.GetClassName(hwnd)
        self.edt_hwnd.setText(self.hwnd_str)
        self.edt_wnd_title.setText(window_title)
        self.edt_wnd_class.setText(window_class)
        # 获取 pid 和 tid
        tid, pid = win32process.GetWindowThreadProcessId(hwnd)
        if self.chk_pid_hex.isChecked():
            self.edt_pid.setText(HexStr(pid))
        else:
            self.edt_pid.setText(str(pid))
        if self.chk_tid_hex.isChecked():
            self.edt_tid.setText(HexStr(tid))
        else:
            self.edt_tid.setText(str(tid))
        # 获取模块路径
        h_process = win32api.OpenProcess(
            win32con.PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if h_process:
            exe_path = win32process.GetModuleFileNameEx(h_process, 0)
            self.edt_exe_path.setText(exe_path)
        # 获取窗口大小
        rect = win32gui.GetWindowRect(hwnd)
        w = rect[2] - rect[0]
        h = rect[3] - rect[1]
        self.edt_wnd_size.setText(f'宽:{w} x 高:{h}')
        # 获取窗口客户区大小
        rect = win32gui.GetClientRect(hwnd)
        w = rect[2] - rect[0]
        h = rect[3] - rect[1]
        self.edt_client_size.setText(f'宽:{w} x 高:{h}')

    def on_chk_hwnd_hex_changed(self, state: int):
        hwnd_str = self.edt_hwnd.text()
        if not hwnd_str:
            self.edt_hwnd.setText('')
            return
        if state == Qt.Checked:
            self.edt_hwnd.setText(HexStr(int(hwnd_str)))
        else:
            self.edt_hwnd.setText(str(int(hwnd_str, 16)))

    def on_chk_pid_hex_changed(self, state: int):
        pid_str = self.edt_pid.text()
        if not pid_str:
            self.edt_pid.setText('')
            return
        if state == Qt.Checked:
            self.edt_pid.setText(HexStr(int(pid_str)))
        else:
            self.edt_pid.setText(str(int(pid_str, 16)))
    def on_chk_tid_hex_changed(self, state: int):
        tid_str = self.edt_tid.text()
        if not tid_str:
            self.edt_tid.setText('')
            return
        if state == Qt.Checked:
            self.edt_tid.setText(HexStr(int(tid_str)))
        else:
            self.edt_tid.setText(str(int(tid_str, 16)))

    
    
    def closeEvent(self, event: QCloseEvent):
        self.save_config()
        return super().closeEvent(event)
    
    def save_config(self):
        config_dict = {
            self.chk_hwnd_hex.objectName(): self.chk_hwnd_hex.isChecked(),
            self.chk_pid_hex.objectName(): self.chk_pid_hex.isChecked(),
            self.chk_tid_hex.objectName(): self.chk_tid_hex.isChecked(),
        }
        # 保存到文件
        with open(self.config_path, 'w') as f:
            json.dump(config_dict, f)

    def read_config(self):
        config_dict = {}
        if not os.path.exists(self.config_path):
            return
        with open(self.config_path, 'r') as f:
            config_dict = json.load(f)
        for key, value in config_dict.items():
            if key.startswith('chk_'):
                eval(f'self.{key}.setChecked({value})')

