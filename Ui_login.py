# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\login.ui'
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

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        DialogLogin.setObjectName(_fromUtf8("DialogLogin"))
        DialogLogin.resize(600, 500)
        DialogLogin.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(DialogLogin)
        self.label.setGeometry(QtCore.QRect(130, 80, 371, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DialogLogin)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 51, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DialogLogin)
        self.label_3.setGeometry(QtCore.QRect(90, 250, 51, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_login = QtGui.QPushButton(DialogLogin)
        self.pushButton_login.setGeometry(QtCore.QRect(150, 360, 93, 28))
        self.pushButton_login.setDefault(True)
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.pushButton_exit = QtGui.QPushButton(DialogLogin)
        self.pushButton_exit.setGeometry(QtCore.QRect(350, 360, 93, 28))
        self.pushButton_exit.setObjectName(_fromUtf8("pushButton_exit"))
        self.lineEdit_password = QtGui.QLineEdit(DialogLogin)
        self.lineEdit_password.setGeometry(QtCore.QRect(280, 250, 201, 31))
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.lineEdit_user = QtGui.QLineEdit(DialogLogin)
        self.lineEdit_user.setGeometry(QtCore.QRect(280, 190, 201, 31))
        self.lineEdit_user.setObjectName(_fromUtf8("lineEdit_user"))

        self.retranslateUi(DialogLogin)
        QtCore.QObject.connect(self.pushButton_exit, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogLogin.close)
        QtCore.QMetaObject.connectSlotsByName(DialogLogin)

    def retranslateUi(self, DialogLogin):
        DialogLogin.setWindowTitle(_translate("DialogLogin", "人事档案管理系统", None))
        self.label.setText(_translate("DialogLogin", "欢迎进入人事档案管理系统", None))
        self.label_2.setText(_translate("DialogLogin", "用户名", None))
        self.label_3.setText(_translate("DialogLogin", "密码", None))
        self.pushButton_login.setText(_translate("DialogLogin", "登录", None))
        self.pushButton_exit.setText(_translate("DialogLogin", "退出", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogLogin = QtGui.QDialog()
    ui = Ui_DialogLogin()
    ui.setupUi(DialogLogin)
    DialogLogin.show()
    sys.exit(app.exec_())

