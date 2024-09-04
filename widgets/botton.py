import os
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt
from memwin import XWinAPI, XWinCon


class AttachButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.on_btn_attach_pressed()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.on_btn_attach_released()
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, e: QMouseEvent):

        super().mouseMoveEvent(e)

    def on_btn_attach_pressed(self):
        print('on_btn_attach_pressed')
        # 按下后 改变鼠标图标
        path = os.path.join(os.getcwd(), 'ui', 'search.cur')
        hCursorNew = XWinAPI.LoadImage(
            None, path, XWinCon.IMAGE_CURSOR, 32, 32, XWinCon.LR_LOADFROMFILE)
        print(f'hCursorNew: {hCursorNew}')
        if hCursorNew:
            XWinAPI.SetSystemCursor(hCursorNew, XWinCon.OCR_NORMAL)

    def on_btn_attach_released(self):
        print('on_btn_attach_released')
        # 监控鼠标松开 恢复鼠标默认图标
        path = os.path.join(os.getcwd(), 'ui', 'aero_arrow.cur')
        hCursor = XWinAPI.LoadImage(
            None, path, XWinCon.IMAGE_CURSOR, 32, 32, XWinCon.LR_LOADFROMFILE)
        XWinAPI.SetSystemCursor(hCursor, XWinCon.OCR_NORMAL)
