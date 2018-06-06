# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\manage_database.ui'
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

class Ui_ManageDatabaseWindow(object):
    def setupUi(self, ManageDatabaseWindow):
        ManageDatabaseWindow.setObjectName(_fromUtf8("ManageDatabaseWindow"))
        ManageDatabaseWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ManageDatabaseWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lineEdit_beifen = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_beifen.setGeometry(QtCore.QRect(260, 200, 231, 51))
        self.lineEdit_beifen.setObjectName(_fromUtf8("lineEdit_beifen"))
        self.lineEdit_huifu = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_huifu.setGeometry(QtCore.QRect(260, 310, 231, 51))
        self.lineEdit_huifu.setObjectName(_fromUtf8("lineEdit_huifu"))
        self.pushButton_beifen = QtGui.QPushButton(self.centralWidget)
        self.pushButton_beifen.setGeometry(QtCore.QRect(570, 200, 181, 51))
        self.pushButton_beifen.setObjectName(_fromUtf8("pushButton_beifen"))
        self.pushButton_huifu = QtGui.QPushButton(self.centralWidget)
        self.pushButton_huifu.setGeometry(QtCore.QRect(570, 320, 181, 51))
        self.pushButton_huifu.setObjectName(_fromUtf8("pushButton_huifu"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 200, 171, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 171, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        ManageDatabaseWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(ManageDatabaseWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageDatabaseWindow)

    def retranslateUi(self, ManageDatabaseWindow):
        ManageDatabaseWindow.setWindowTitle(_translate("ManageDatabaseWindow", "ManageDatabaseWindow", None))
        self.pushButton_beifen.setText(_translate("ManageDatabaseWindow", "备份", None))
        self.pushButton_huifu.setText(_translate("ManageDatabaseWindow", "恢复", None))
        self.label.setText(_translate("ManageDatabaseWindow", "数据库备份，请输入名称", None))
        self.label_2.setText(_translate("ManageDatabaseWindow", "数据库恢复，请输入名称", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ManageDatabaseWindow = QtGui.QMainWindow()
    ui = Ui_ManageDatabaseWindow()
    ui.setupUi(ManageDatabaseWindow)
    ManageDatabaseWindow.show()
    sys.exit(app.exec_())

