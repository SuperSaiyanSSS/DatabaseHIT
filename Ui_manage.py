# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\manage.ui'
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

class Ui_ManageWindow(object):
    def setupUi(self, ManageWindow):
        ManageWindow.setObjectName(_fromUtf8("ManageWindow"))
        ManageWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ManageWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_table = QtGui.QPushButton(self.centralWidget)
        self.pushButton_table.setGeometry(QtCore.QRect(270, 80, 191, 91))
        self.pushButton_table.setObjectName(_fromUtf8("pushButton_table"))
        self.pushButton_user = QtGui.QPushButton(self.centralWidget)
        self.pushButton_user.setGeometry(QtCore.QRect(270, 250, 191, 91))
        self.pushButton_user.setObjectName(_fromUtf8("pushButton_user"))
        self.pushButton_database = QtGui.QPushButton(self.centralWidget)
        self.pushButton_database.setGeometry(QtCore.QRect(270, 430, 191, 91))
        self.pushButton_database.setObjectName(_fromUtf8("pushButton_database"))
        ManageWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(ManageWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageWindow)

    def retranslateUi(self, ManageWindow):
        ManageWindow.setWindowTitle(_translate("ManageWindow", "ManageWindow", None))
        self.pushButton_table.setText(_translate("ManageWindow", "编码表管理", None))
        self.pushButton_user.setText(_translate("ManageWindow", "用户管理", None))
        self.pushButton_database.setText(_translate("ManageWindow", "数据库备份", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ManageWindow = QtGui.QMainWindow()
    ui = Ui_ManageWindow()
    ui.setupUi(ManageWindow)
    ManageWindow.show()
    sys.exit(app.exec_())

