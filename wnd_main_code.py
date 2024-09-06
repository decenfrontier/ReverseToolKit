import json
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from memwin import *
import win32gui

from ui.wnd_main import Ui_WndMain
from widgets.botton import AttachButton



class WndMain(QMainWindow, Ui_WndMain):
    sig_hwnd_changed = Signal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.config_path = os.path.join(os.getenv('APPDATA'), 'config.json')
        self.hwnd_str = ''
        self.init_widgets()
        self.read_config()
        self.init_sig_slots()

    def init_widgets(self):
        self.btn_attach.__class__ = AttachButton
        self.btn_attach.setText('🔍')
        self.btn_attach.setFont(QFont('Segoe UI', 15))

    def init_sig_slots(self):
        self.sig_hwnd_changed.connect(self.on_hwnd_changed)
        self.chk_hwnd_hex.stateChanged.connect(self.on_chk_hwnd_hex_changed)

    def on_hwnd_changed(self, hwnd: int):
        if self.chk_hwnd_hex.isChecked():
            self.hwnd_str = hex(hwnd)
            print(f'self.hwnd: {self.hwnd_str}')
        else:
            self.hwnd_str = str(hwnd)
        window_title = win32gui.GetWindowText(hwnd)
        window_class = win32gui.GetClassName(hwnd)
        self.edt_hwnd.setText(self.hwnd_str)
        self.edt_wnd_title.setText(window_title)
        self.edt_wnd_class.setText(window_class)

    def on_chk_hwnd_hex_changed(self, state: int):
        if state == Qt.Checked:
            self.edt_hwnd.setText(hex(int(self.edt_hwnd.text())))
        else:
            self.edt_hwnd.setText(str(int(self.edt_hwnd.text(), 16)))
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.save_config()
        return super().closeEvent(event)
    
    def save_config(self):
        settings = {}
        # 假设你有一个布局中的所有控件列表
        for widget in self.centralwidget.children():
            if isinstance(widget, (QCheckBox, QSpinBox)):
                if isinstance(widget, QLineEdit):
                    settings[widget.objectName()] = widget.text()
                elif isinstance(widget, QCheckBox):
                    settings[widget.objectName()] = widget.isChecked()
                elif isinstance(widget, QSpinBox):
                    settings[widget.objectName()] = widget.value()
        # 保存到文件
        with open(self.config_path, 'w') as f:
            json.dump(settings, f)

    def read_config(self):
        settings = {}
        if not os.path.exists(self.config_path):
            return
        with open(self.config_path, 'r') as f:
            settings = json.load(f)
        for widget in self.centralwidget.children():
            if isinstance(widget, (QCheckBox, QSpinBox)):
                if widget.objectName() not in settings:
                    continue
                if isinstance(widget, QLineEdit):
                    widget.setText(settings[widget.objectName()])
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(settings[widget.objectName()])
                elif isinstance(widget, QSpinBox):
                    widget.setValue(settings[widget.objectName()])
        
