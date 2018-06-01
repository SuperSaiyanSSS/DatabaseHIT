# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton_add = QtGui.QPushButton(self.centralWidget)
        self.pushButton_add.setGeometry(QtCore.QRect(170, 160, 161, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_view = QtGui.QPushButton(self.centralWidget)
        self.pushButton_view.setGeometry(QtCore.QRect(420, 160, 161, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_view.setFont(font)
        self.pushButton_view.setObjectName(_fromUtf8("pushButton_view"))
        self.pushButton_analyse = QtGui.QPushButton(self.centralWidget)
        self.pushButton_analyse.setGeometry(QtCore.QRect(170, 300, 161, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_analyse.setFont(font)
        self.pushButton_analyse.setObjectName(_fromUtf8("pushButton_analyse"))
        self.pushButton_manage = QtGui.QPushButton(self.centralWidget)
        self.pushButton_manage.setGeometry(QtCore.QRect(420, 300, 161, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(14)
        self.pushButton_manage.setFont(font)
        self.pushButton_manage.setObjectName(_fromUtf8("pushButton_manage"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_add.setText(_translate("MainWindow", "档案录入", None))
        self.pushButton_view.setText(_translate("MainWindow", "查看编辑", None))
        self.pushButton_analyse.setText(_translate("MainWindow", "统计报表", None))
        self.pushButton_manage.setText(_translate("MainWindow", "系统管理", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

