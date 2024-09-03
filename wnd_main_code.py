import json
import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.wnd_main import Ui_WndMain


class WndMain(QMainWindow, Ui_WndMain):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.config_path = os.path.join(os.getenv('APPDATA'), 'config.json')
        self.read_config()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.save_config()
        return super().closeEvent(event)
    
    def save_config(self):
        settings = {}
        # 假设你有一个布局中的所有控件列表
        for widget in self.centralwidget.children():
            if isinstance(widget, (QLineEdit, QCheckBox, QSpinBox)):
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
            if isinstance(widget, (QLineEdit, QCheckBox, QSpinBox)):
                if widget.objectName() not in settings:
                    continue
                if isinstance(widget, QLineEdit):
                    widget.setText(settings[widget.objectName()])
                elif isinstance(widget, QCheckBox):
                    widget.setChecked(settings[widget.objectName()])
                elif isinstance(widget, QSpinBox):
                    widget.setValue(settings[widget.objectName()])
        
