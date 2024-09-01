import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import *

from ui.wnd_main import Ui_WndMain


class WndMain(QMainWindow, Ui_WndMain):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def closeEvent(self, event: QCloseEvent) -> None:
        roaming_path = os.getenv('APPDATA')
        # TODO: 保存配置
        
        return super().closeEvent(event)