# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Weather.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(401, 340))
        Form.setMaximumSize(QtCore.QSize(401, 340))
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 230, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 270, 361, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 200, 381, 121))
        self.frame.setStyleSheet("border:1px solid rgb(0, 0, 0)\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label_tempeture_1 = QtWidgets.QLabel(self.frame)
        self.label_tempeture_1.setGeometry(QtCore.QRect(310, 10, 61, 21))
        self.label_tempeture_1.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_tempeture_1.setObjectName("label_tempeture_1")
        self.label_weather_1 = QtWidgets.QLabel(self.frame)
        self.label_weather_1.setGeometry(QtCore.QRect(60, 10, 101, 21))
        self.label_weather_1.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_weather_1.setObjectName("label_weather_1")
        self.label_weather_2 = QtWidgets.QLabel(self.frame)
        self.label_weather_2.setGeometry(QtCore.QRect(60, 50, 101, 21))
        self.label_weather_2.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_weather_2.setObjectName("label_weather_2")
        self.label_weather_3 = QtWidgets.QLabel(self.frame)
        self.label_weather_3.setGeometry(QtCore.QRect(60, 90, 101, 21))
        self.label_weather_3.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_weather_3.setObjectName("label_weather_3")
        self.label_date_3 = QtWidgets.QLabel(self.frame)
        self.label_date_3.setGeometry(QtCore.QRect(20, 90, 31, 21))
        self.label_date_3.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_date_3.setObjectName("label_date_3")
        self.label_date_1 = QtWidgets.QLabel(self.frame)
        self.label_date_1.setGeometry(QtCore.QRect(20, 10, 31, 21))
        self.label_date_1.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_date_1.setObjectName("label_date_1")
        self.label_date_2 = QtWidgets.QLabel(self.frame)
        self.label_date_2.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.label_date_2.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_date_2.setObjectName("label_date_2")
        self.label_tempeture_2 = QtWidgets.QLabel(self.frame)
        self.label_tempeture_2.setGeometry(QtCore.QRect(310, 50, 61, 21))
        self.label_tempeture_2.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_tempeture_2.setObjectName("label_tempeture_2")
        self.label_tempeture_3 = QtWidgets.QLabel(self.frame)
        self.label_tempeture_3.setGeometry(QtCore.QRect(310, 90, 61, 21))
        self.label_tempeture_3.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_tempeture_3.setObjectName("label_tempeture_3")
        self.label_picture_1 = QtWidgets.QLabel(self.frame)
        self.label_picture_1.setGeometry(QtCore.QRect(250, 10, 31, 21))
        self.label_picture_1.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_picture_1.setObjectName("label_picture_1")
        self.label_picture_2 = QtWidgets.QLabel(self.frame)
        self.label_picture_2.setGeometry(QtCore.QRect(250, 50, 31, 21))
        self.label_picture_2.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_picture_2.setObjectName("label_picture_2")
        self.label_picture_3 = QtWidgets.QLabel(self.frame)
        self.label_picture_3.setGeometry(QtCore.QRect(250, 90, 31, 21))
        self.label_picture_3.setStyleSheet("border:0px solid rgb(0, 0, 0)")
        self.label_picture_3.setObjectName("label_picture_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 40, 381, 151))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_tempeture_0 = QtWidgets.QLabel(self.frame_2)
        self.label_tempeture_0.setGeometry(QtCore.QRect(30, 10, 71, 51))
        self.label_tempeture_0.setObjectName("label_tempeture_0")
        self.label_weather_0 = QtWidgets.QLabel(self.frame_2)
        self.label_weather_0.setGeometry(QtCore.QRect(20, 60, 171, 51))
        self.label_weather_0.setObjectName("label_weather_0")
        self.label_celcius = QtWidgets.QLabel(self.frame_2)
        self.label_celcius.setGeometry(QtCore.QRect(80, 10, 21, 21))
        self.label_celcius.setObjectName("label_celcius")
        self.label_api_0 = QtWidgets.QLabel(self.frame_2)
        self.label_api_0.setGeometry(QtCore.QRect(20, 100, 171, 51))
        self.label_api_0.setObjectName("label_api_0")
        self.label_picture_0 = QtWidgets.QLabel(self.frame_2)
        self.label_picture_0.setGeometry(QtCore.QRect(230, 31, 111, 81))
        self.label_picture_0.setObjectName("label_picture_0")
        self.label_location = QtWidgets.QLabel(Form)
        self.label_location.setGeometry(QtCore.QRect(180, 10, 121, 21))
        self.label_location.setObjectName("label_location")
        self.button_changeLocation = QtWidgets.QPushButton(Form)
        self.button_changeLocation.setGeometry(QtCore.QRect(20, 10, 21, 23))
        self.button_changeLocation.setObjectName("button_changeLocation")
        self.button_change_init_location = QtWidgets.QPushButton(Form)
        self.button_change_init_location.setGeometry(QtCore.QRect(360, 10, 21, 23))
        self.button_change_init_location.setObjectName("button_change_init_location")
        self.frame.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.frame_2.raise_()
        self.label_location.raise_()
        self.button_changeLocation.raise_()
        self.button_change_init_location.raise_()

        self.retranslateUi(Form)
        self.button_changeLocation.clicked.connect(Form.button_click_input)
        self.button_change_init_location.clicked.connect(Form.change_init_city)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_tempeture_1.setText(_translate("Form", "<html><head/><body><p>15 / 5℃</p></body></html>"))
        self.label_weather_1.setText(_translate("Form", "<html><head/><body><p>多云</p></body></html>"))
        self.label_weather_2.setText(_translate("Form", "<html><head/><body><p>多云</p></body></html>"))
        self.label_weather_3.setText(_translate("Form", "<html><head/><body><p>大暴雨到特大暴雨</p></body></html>"))
        self.label_date_3.setText(_translate("Form", "<html><head/><body><p>后天·</p></body></html>"))
        self.label_date_1.setText(_translate("Form", "<html><head/><body><p>今天·</p></body></html>"))
        self.label_date_2.setText(_translate("Form", "<html><head/><body><p>明天·</p></body></html>"))
        self.label_tempeture_2.setText(_translate("Form", "<html><head/><body><p>15 / 5℃</p></body></html>"))
        self.label_tempeture_3.setText(_translate("Form", "<html><head/><body><p>15 / 5℃</p></body></html>"))
        self.label_picture_1.setText(_translate("Form", "<html><head/><body><p>图片</p></body></html>"))
        self.label_picture_2.setText(_translate("Form", "<html><head/><body><p>图片</p></body></html>"))
        self.label_picture_3.setText(_translate("Form", "<html><head/><body><p>图片</p></body></html>"))
        self.label_tempeture_0.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt;\">14</span></p></body></html>"))
        self.label_weather_0.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">多云</span></p></body></html>"))
        self.label_celcius.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">℃</span></p></body></html>"))
        self.label_api_0.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">空气优 50</span></p></body></html>"))
        self.label_picture_0.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">图片</span></p></body></html>"))
        self.label_location.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">合肥</span></p></body></html>"))
        self.button_changeLocation.setText(_translate("Form", "+"))
        self.button_change_init_location.setText(_translate("Form", "·"))

