# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\manage_user.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ManageUserWindow(object):
    def setupUi(self, ManageUserWindow):
        ManageUserWindow.setObjectName(_fromUtf8("ManageUserWindow"))
        ManageUserWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ManageUserWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lineEdit_last = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_last.setGeometry(QtCore.QRect(200, 150, 321, 51))
        self.lineEdit_last.setObjectName(_fromUtf8("lineEdit_last"))
        self.lineEdit_new1 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_new1.setGeometry(QtCore.QRect(200, 300, 321, 51))
        self.lineEdit_new1.setObjectName(_fromUtf8("lineEdit_new1"))
        self.lineEdit_new2 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_new2.setGeometry(QtCore.QRect(200, 460, 321, 51))
        self.lineEdit_new2.setObjectName(_fromUtf8("lineEdit_new2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 90, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 240, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(200, 400, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 470, 141, 71))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ManageUserWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(ManageUserWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageUserWindow)

    def retranslateUi(self, ManageUserWindow):
        ManageUserWindow.setWindowTitle(_translate("ManageUserWindow", "ManageUserWindow", None))
        self.label.setText(_translate("ManageUserWindow", "请输入您的原密码", None))
        self.label_2.setText(_translate("ManageUserWindow", "请输入新密码", None))
        self.label_3.setText(_translate("ManageUserWindow", "请再次输入新密码，确保一致", None))
        self.pushButton.setText(_translate("ManageUserWindow", "修改", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ManageUserWindow = QtGui.QMainWindow()
    ui = Ui_ManageUserWindow()
    ui.setupUi(ManageUserWindow)
    ManageUserWindow.show()
    sys.exit(app.exec_())

