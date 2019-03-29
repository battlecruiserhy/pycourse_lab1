# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Query.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Query_Form(object):
    def setupUi(self, Query_Form):
        Query_Form.setObjectName("Query_Form")
        Query_Form.resize(401, 340)
        Query_Form.setMinimumSize(QtCore.QSize(401, 340))
        Query_Form.setMaximumSize(QtCore.QSize(401, 340))
        self.label = QtWidgets.QLabel(Query_Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 41))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Query_Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 120, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Query_Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Query_Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 351, 51))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Query_Form)
        self.pushButton.clicked.connect(Query_Form.button_click_confirm)
        QtCore.QMetaObject.connectSlotsByName(Query_Form)

    def retranslateUi(self, Query_Form):
        _translate = QtCore.QCoreApplication.translate
        Query_Form.setWindowTitle(_translate("Query_Form", "Form"))
        self.label.setText(_translate("Query_Form", "<html><head/><body><p><span style=\" font-size:14pt;\">搜索国内城市</span></p></body></html>"))
        self.pushButton.setText(_translate("Query_Form", "确定"))
        self.label_2.setText(_translate("Query_Form", "<html><head/><body><p><br/></p></body></html>"))

