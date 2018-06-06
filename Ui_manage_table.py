# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\manage_table.ui'
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

class Ui_ManageTableWindow(object):
    def setupUi(self, ManageTableWindow):
        ManageTableWindow.setObjectName(_fromUtf8("ManageTableWindow"))
        ManageTableWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ManageTableWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.comboBox = QtGui.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 70, 201, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit_code = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_code.setGeometry(QtCore.QRect(70, 220, 201, 41))
        self.lineEdit_code.setObjectName(_fromUtf8("lineEdit_code"))
        self.lineEdit_content = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_content.setGeometry(QtCore.QRect(70, 300, 201, 41))
        self.lineEdit_content.setObjectName(_fromUtf8("lineEdit_content"))
        self.pushButton_add = QtGui.QPushButton(self.centralWidget)
        self.pushButton_add.setGeometry(QtCore.QRect(70, 390, 201, 41))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_delete = QtGui.QPushButton(self.centralWidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(70, 480, 201, 41))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 70, 391, 451))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_view = QtGui.QPushButton(self.centralWidget)
        self.pushButton_view.setGeometry(QtCore.QRect(70, 140, 201, 41))
        self.pushButton_view.setObjectName(_fromUtf8("pushButton_view"))
        ManageTableWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(ManageTableWindow)
        QtCore.QMetaObject.connectSlotsByName(ManageTableWindow)

    def retranslateUi(self, ManageTableWindow):
        ManageTableWindow.setWindowTitle(_translate("ManageTableWindow", "ManageTableWindow", None))
        self.pushButton_add.setText(_translate("ManageTableWindow", "增加", None))
        self.pushButton_delete.setText(_translate("ManageTableWindow", "删除", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManageTableWindow", "编码", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManageTableWindow", "内容", None))
        self.pushButton_view.setText(_translate("ManageTableWindow", "查看", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ManageTableWindow = QtGui.QMainWindow()
    ui = Ui_ManageTableWindow()
    ui.setupUi(ManageTableWindow)
    ManageTableWindow.show()
    sys.exit(app.exec_())

