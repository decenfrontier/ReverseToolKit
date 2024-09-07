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
        WndMain.resize(378, 391)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_attach = QToolButton(self.centralwidget)
        self.btn_attach.setObjectName(u"btn_attach")
        self.btn_attach.setMinimumSize(QSize(45, 35))
        self.btn_attach.setMaximumSize(QSize(45, 35))

        self.horizontalLayout_7.addWidget(self.btn_attach)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edt_hwnd = QLineEdit(self.centralwidget)
        self.edt_hwnd.setObjectName(u"edt_hwnd")
        self.edt_hwnd.setMinimumSize(QSize(66, 0))
        self.edt_hwnd.setMaximumSize(QSize(66, 16777215))

        self.horizontalLayout.addWidget(self.edt_hwnd)

        self.chk_hwnd_hex = QCheckBox(self.centralwidget)
        self.chk_hwnd_hex.setObjectName(u"chk_hwnd_hex")

        self.horizontalLayout.addWidget(self.chk_hwnd_hex)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.edt_wnd_title = QLineEdit(self.tab)
        self.edt_wnd_title.setObjectName(u"edt_wnd_title")
        self.edt_wnd_title.setReadOnly(True)
        self.edt_wnd_title.setClearButtonEnabled(False)

        self.horizontalLayout_6.addWidget(self.edt_wnd_title)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.edt_wnd_class = QLineEdit(self.tab)
        self.edt_wnd_class.setObjectName(u"edt_wnd_class")
        self.edt_wnd_class.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.edt_wnd_class)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.edt_pid = QLineEdit(self.tab)
        self.edt_pid.setObjectName(u"edt_pid")
        self.edt_pid.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.edt_pid)

        self.chk_pid_hex = QCheckBox(self.tab)
        self.chk_pid_hex.setObjectName(u"chk_pid_hex")

        self.horizontalLayout_4.addWidget(self.chk_pid_hex)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.edt_tid = QLineEdit(self.tab)
        self.edt_tid.setObjectName(u"edt_tid")
        self.edt_tid.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.edt_tid)

        self.chk_tid_hex = QCheckBox(self.tab)
        self.chk_tid_hex.setObjectName(u"chk_tid_hex")

        self.horizontalLayout_3.addWidget(self.chk_tid_hex)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.edt_exe_path = QLineEdit(self.tab)
        self.edt_exe_path.setObjectName(u"edt_exe_path")
        self.edt_exe_path.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.edt_exe_path)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.edt_wnd_size = QLineEdit(self.tab)
        self.edt_wnd_size.setObjectName(u"edt_wnd_size")
        self.edt_wnd_size.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.edt_wnd_size)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.edt_client_size = QLineEdit(self.tab)
        self.edt_client_size.setObjectName(u"edt_client_size")
        self.edt_client_size.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.edt_client_size)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.textEdit = QTextEdit(self.tab_2)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_10.addWidget(self.textEdit)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        WndMain.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WndMain)
        self.statusbar.setObjectName(u"statusbar")
        WndMain.setStatusBar(self.statusbar)

        self.retranslateUi(WndMain)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"DC Reserve ToolKit", None))
        self.btn_attach.setText("")
        self.label_7.setText(QCoreApplication.translate("WndMain", u"\u6309\u4e0b\u62d6\u52a8\u5230\u6307\u5b9a\u7a97\u53e3", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u53e5\u67c4", None))
        self.chk_hwnd_hex.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u6807\u9898", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u7c7b\u540d", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u8fdb\u7a0bID(PID)", None))
        self.chk_pid_hex.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u7ebf\u7a0bID(TID)", None))
        self.chk_tid_hex.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u6a21\u5757\u8def\u5f84", None))
        self.edt_exe_path.setText("")
        self.label_9.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u5927\u5c0f", None))
        self.edt_wnd_size.setText("")
        self.label_10.setText(QCoreApplication.translate("WndMain", u"\u5ba2\u6237\u533a\u5927\u5c0f", None))
        self.edt_client_size.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u4fe1\u606f", None))
        self.pushButton.setText(QCoreApplication.translate("WndMain", u"Call", None))
        self.pushButton_2.setText(QCoreApplication.translate("WndMain", u"\u7533\u8bf7\u5185\u5b58", None))
        self.label_8.setText(QCoreApplication.translate("WndMain", u"\u6267\u884c\u7ed3\u679c:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("WndMain", u"\u4ee3\u7801\u6ce8\u5165", None))
    # retranslateUi

