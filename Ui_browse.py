# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\DatabaseHIT\browse.ui'
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

class Ui_BrowseWindow(object):
    def setupUi(self, BrowseWindow):
        BrowseWindow.setObjectName(_fromUtf8("BrowseWindow"))
        BrowseWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(BrowseWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 230, 771, 341))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(31)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        self.pushButton_find_id_accurately = QtGui.QPushButton(self.centralWidget)
        self.pushButton_find_id_accurately.setGeometry(QtCore.QRect(430, 20, 131, 41))
        self.pushButton_find_id_accurately.setObjectName(_fromUtf8("pushButton_find_id_accurately"))
        self.pushButton_find_id_vaguely = QtGui.QPushButton(self.centralWidget)
        self.pushButton_find_id_vaguely.setGeometry(QtCore.QRect(610, 20, 131, 41))
        self.pushButton_find_id_vaguely.setObjectName(_fromUtf8("pushButton_find_id_vaguely"))
        self.pushButton_find_name_accurately = QtGui.QPushButton(self.centralWidget)
        self.pushButton_find_name_accurately.setGeometry(QtCore.QRect(430, 80, 131, 41))
        self.pushButton_find_name_accurately.setObjectName(_fromUtf8("pushButton_find_name_accurately"))
        self.pushButton_find_name_vaguely = QtGui.QPushButton(self.centralWidget)
        self.pushButton_find_name_vaguely.setGeometry(QtCore.QRect(610, 80, 131, 41))
        self.pushButton_find_name_vaguely.setObjectName(_fromUtf8("pushButton_find_name_vaguely"))
        self.textEdit_find = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_find.setGeometry(QtCore.QRect(70, 20, 261, 51))
        self.textEdit_find.setObjectName(_fromUtf8("textEdit_find"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(70, 130, 641, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit_id = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_id.setGeometry(QtCore.QRect(430, 170, 131, 41))
        self.textEdit_id.setObjectName(_fromUtf8("textEdit_id"))
        self.pushButton_update = QtGui.QPushButton(self.centralWidget)
        self.pushButton_update.setGeometry(QtCore.QRect(70, 170, 131, 41))
        self.pushButton_update.setObjectName(_fromUtf8("pushButton_update"))
        self.pushButton_delete = QtGui.QPushButton(self.centralWidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(200, 170, 131, 41))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.pushButton_view_person = QtGui.QPushButton(self.centralWidget)
        self.pushButton_view_person.setGeometry(QtCore.QRect(610, 170, 131, 41))
        self.pushButton_view_person.setObjectName(_fromUtf8("pushButton_view_person"))
        BrowseWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(BrowseWindow)
        QtCore.QMetaObject.connectSlotsByName(BrowseWindow)

    def retranslateUi(self, BrowseWindow):
        BrowseWindow.setWindowTitle(_translate("BrowseWindow", "档案浏览", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BrowseWindow", "职工编码", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BrowseWindow", "姓名", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BrowseWindow", "性别", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BrowseWindow", "民族", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BrowseWindow", "出生年月", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BrowseWindow", "婚姻状况", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("BrowseWindow", "文化程度", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("BrowseWindow", "健康状况", None))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("BrowseWindow", "政治面貌", None))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("BrowseWindow", "职称", None))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("BrowseWindow", "籍贯", None))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("BrowseWindow", "身份证号码", None))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("BrowseWindow", "毕业学校", None))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("BrowseWindow", "专业或特长", None))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("BrowseWindow", "户口所在地", None))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("BrowseWindow", "户口性质", None))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("BrowseWindow", "现住址", None))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("BrowseWindow", "职务", None))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("BrowseWindow", "工种名", None))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("BrowseWindow", "何时技术培训", None))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("BrowseWindow", "何时奖励和处分", None))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("BrowseWindow", "需要说明问题", None))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("BrowseWindow", "填表人签名", None))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("BrowseWindow", "填表日期", None))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("BrowseWindow", "公司审查意见", None))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("BrowseWindow", "审查日期", None))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("BrowseWindow", "人员性质", None))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("BrowseWindow", "入常时间", None))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("BrowseWindow", "人员状态", None))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("BrowseWindow", "备注", None))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("BrowseWindow", "部门", None))
        self.pushButton_find_id_accurately.setText(_translate("BrowseWindow", "编号精确查找", None))
        self.pushButton_find_id_vaguely.setText(_translate("BrowseWindow", "编号模糊查找", None))
        self.pushButton_find_name_accurately.setText(_translate("BrowseWindow", "姓名精确查找", None))
        self.pushButton_find_name_vaguely.setText(_translate("BrowseWindow", "姓名模糊查找", None))
        self.label.setText(_translate("BrowseWindow", "--------------------------------------------------------------------------------", None))
        self.pushButton_update.setText(_translate("BrowseWindow", "更新档案", None))
        self.pushButton_delete.setText(_translate("BrowseWindow", "删除档案", None))
        self.pushButton_view_person.setText(_translate("BrowseWindow", "查看具体个人档案", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    BrowseWindow = QtGui.QMainWindow()
    ui = Ui_BrowseWindow()
    ui.setupUi(BrowseWindow)
    BrowseWindow.show()
    sys.exit(app.exec_())

