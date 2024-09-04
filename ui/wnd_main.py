# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(303, 290)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_attach = QToolButton(self.centralwidget)
        self.btn_attach.setObjectName(u"btn_attach")
        self.btn_attach.setMinimumSize(QSize(45, 35))
        self.btn_attach.setMaximumSize(QSize(45, 35))

        self.horizontalLayout_7.addWidget(self.btn_attach)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edt_hwnd = QLineEdit(self.centralwidget)
        self.edt_hwnd.setObjectName(u"edt_hwnd")

        self.horizontalLayout.addWidget(self.edt_hwnd)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.edt_wnd_title = QLineEdit(self.centralwidget)
        self.edt_wnd_title.setObjectName(u"edt_wnd_title")

        self.horizontalLayout_6.addWidget(self.edt_wnd_title)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.edt_wnd_class = QLineEdit(self.centralwidget)
        self.edt_wnd_class.setObjectName(u"edt_wnd_class")

        self.horizontalLayout_5.addWidget(self.edt_wnd_class)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.edt_pid = QLineEdit(self.centralwidget)
        self.edt_pid.setObjectName(u"edt_pid")

        self.horizontalLayout_4.addWidget(self.edt_pid)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_4.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.edt_tid = QLineEdit(self.centralwidget)
        self.edt_tid.setObjectName(u"edt_tid")

        self.horizontalLayout_3.addWidget(self.edt_tid)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_3.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.edt_hmodule = QLineEdit(self.centralwidget)
        self.edt_hmodule.setObjectName(u"edt_hmodule")

        self.horizontalLayout_2.addWidget(self.edt_hmodule)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        WndMain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WndMain)
        self.statusbar.setObjectName(u"statusbar")
        WndMain.setStatusBar(self.statusbar)

        self.retranslateUi(WndMain)

        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"DC Reserve ToolKit", None))
        self.btn_attach.setText("")
        self.label_7.setText(QCoreApplication.translate("WndMain", u"-- \u6309\u4e0b\u62d6\u52a8\u5230\u6307\u5b9a\u7a97\u53e3 --", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u53e5\u67c4", None))
        self.checkBox_3.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u6807\u9898", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u7c7b\u540d", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u8fdb\u7a0bID(PID)", None))
        self.checkBox.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u7ebf\u7a0bID(TID)", None))
        self.checkBox_2.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u6a21\u5757\u53e5\u67c4", None))
        self.edt_hmodule.setText("")
    # retranslateUi

