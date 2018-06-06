# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing ManageTableWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_manage_table import Ui_ManageTableWindow
import globalvar


class ManageTableWindow(QMainWindow, Ui_ManageTableWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.comboBox.addItems(["职称表", "文化表",  "部门表"])
        self.sql_client = globalvar.get_client()


    def fill_tableview(self, info_tuple):
        self.tableWidget.setRowCount(len(info_tuple))

        for row, line in enumerate(info_tuple):
            for column, item in enumerate(line):
                item = unicode(item)
                item = QTableWidgetItem(item)
                self.tableWidget.setItem(int(row), int(column), item)

    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        code = unicode(self.lineEdit_code.text())
        name = unicode(self.lineEdit_content.text())
        content = unicode(self.comboBox.currentText())
        if content == "职称表":
            self.sql_client.add_zc_info(code, name)
            data = self.sql_client.get_zc_info()
            self.fill_tableview(data)
        elif content == "文化表":
            self.sql_client.add_wh_info(code, name)
            data = self.sql_client.get_wh_info()
            self.fill_tableview(data)
        elif content == "部门表":
            self.sql_client.add_bm_info(code, name)
            data = self.sql_client.get_bm_info()
            self.fill_tableview(data)

    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget.currentIndex().row()
        # 找到对于行的第一项（XX编码项）
        xxbm = unicode(self.tableWidget.takeItem(row, 0).text())
        self.tableWidget.setItem(row, 0, QTableWidgetItem(xxbm))
        content = unicode(self.comboBox.currentText())
        if content == "职称表":
            result_signal = self.sql_client.delete_zc_info(xxbm)
        elif content == "文化表":
            result_signal = self.sql_client.delete_wh_info(xxbm)
        else:
            result_signal = self.sql_client.delete_bm_info(xxbm)

        QMessageBox.information(self, 'Message', "删除成功！", QMessageBox.Yes)
        self.tableWidget.removeRow(row)

    
    @pyqtSignature("")
    def on_pushButton_view_clicked(self):
        """
        Slot documentation goes here.
        """
        content = unicode(self.comboBox.currentText())
        if content == "职称表":
            data = self.sql_client.get_zc_info()
            self.fill_tableview(data)
        elif content == "文化表":
            data = self.sql_client.get_wh_info()
            self.fill_tableview(data)
        elif content == "部门表":
            data = self.sql_client.get_bm_info()
            self.fill_tableview(data)


