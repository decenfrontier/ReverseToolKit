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
        WndMain.resize(588, 297)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 81, 18))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 50, 163, 25))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 90, 163, 25))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 81, 18))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 111, 21))
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 130, 101, 31))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(230, 133, 71, 21))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(230, 170, 71, 21))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(120, 167, 101, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 167, 111, 21))
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(90, 210, 163, 25))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 210, 81, 18))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 301, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.layoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)

        WndMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WndMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 588, 23))
        WndMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WndMain)
        self.statusbar.setObjectName(u"statusbar")
        WndMain.setStatusBar(self.statusbar)

        self.retranslateUi(WndMain)

        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"DC Reserve ToolKit", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u6807\u9898", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u7c7b\u540d", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u8fdb\u7a0bID(PID)", None))
        self.checkBox.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.checkBox_2.setText(QCoreApplication.translate("WndMain", u"16\u8fdb\u5236", None))
        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u7ebf\u7a0bID(TID)", None))
        self.lineEdit_6.setText("")
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u6a21\u5757\u53e5\u67c4", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u53e5\u67c4", None))
        self.toolButton.setText(QCoreApplication.translate("WndMain", u"XXX", None))
    # retranslateUi

