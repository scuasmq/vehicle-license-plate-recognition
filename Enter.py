# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Enter.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Enter(object):
    def setupUi(self, Enter):
        Enter.setObjectName("Enter")
        Enter.setStyleSheet("background-image: url(./pic/face.png);")
        Enter.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        Enter.setObjectName("MainWindow")
        Enter.resize(906, 600)
        Enter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        Enter.setWindowOpacity(0.95)  # 设置窗口透明度
        self.centralwidget = QtWidgets.QWidget(Enter)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 500, 131, 41))
        self.pushButton.setStyleSheet("font: 14pt \"华文琥珀\";\n"
"background-image:transparent;")
        self.pushButton.setObjectName("pushButton")
        Enter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Enter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 22))
        self.menubar.setObjectName("menubar")
        Enter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Enter)
        self.statusbar.setObjectName("statusbar")
        Enter.setStatusBar(self.statusbar)

        self.retranslateUi(Enter)
        QtCore.QMetaObject.connectSlotsByName(Enter)

    def retranslateUi(self, Enter):
        _translate = QtCore.QCoreApplication.translate
        Enter.setWindowTitle(_translate("Enter", "MainWindow"))
        self.pushButton.setText(_translate("Enter", "进入系统"))
import my_pic_rc
z