# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\TexturePackerTool_single\TexturePackerTool_single.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 101)
        Dialog.setMinimumSize(QtCore.QSize(463, 101))
        Dialog.setMaximumSize(QtCore.QSize(463, 101))
        Dialog.setWhatsThis("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.textEdit1 = QtWidgets.QTextEdit(Dialog)
        self.textEdit1.setGeometry(QtCore.QRect(80, 10, 331, 21))
        self.textEdit1.setObjectName("textEdit1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textEdit2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit2.setGeometry(QtCore.QRect(80, 40, 331, 21))
        self.textEdit2.setObjectName("textEdit2")
        self.btnStart = QtWidgets.QPushButton(Dialog)
        self.btnStart.setGeometry(QtCore.QRect(380, 70, 71, 23))
        self.btnStart.setObjectName("btnStart")
        self.btnSelect1 = QtWidgets.QPushButton(Dialog)
        self.btnSelect1.setGeometry(QtCore.QRect(420, 10, 31, 23))
        self.btnSelect1.setObjectName("btnSelect1")
        self.btnSelect2 = QtWidgets.QPushButton(Dialog)
        self.btnSelect2.setGeometry(QtCore.QRect(420, 40, 31, 23))
        self.btnSelect2.setObjectName("btnSelect2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 68, 281, 28))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setToolTip(_translate("Dialog", "用于打单个文件夹的合图"))
        self.label.setText(_translate("Dialog", "合图源:"))
        self.textEdit1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "输出目录:"))
        self.textEdit2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btnStart.setText(_translate("Dialog", "开始合图"))
        self.btnSelect1.setText(_translate("Dialog", "选择"))
        self.btnSelect2.setText(_translate("Dialog", "选择"))
        self.label_3.setText(_translate("Dialog", "使用说明：选择或输入Windows路径后点击开始合图"))
