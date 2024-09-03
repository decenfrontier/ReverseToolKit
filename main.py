import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QStyleFactory
from wnd_main_code import WndMain
import settings


if __name__ == '__main__':
    # 创建应用
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    settings.wnd_main = WndMain()
    settings.wnd_main.show()
    sys.exit(app.exec_())
