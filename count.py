# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing CountWindow.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_count import Ui_CountWindow

import globalvar


class CountWindow(QMainWindow, Ui_CountWindow):
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
        self.sql_client = globalvar.get_client()
        self.label.setText(unicode("当前公司总人数："+unicode(str(self.sql_client.count_sum_people()))))

    def fill_tableview(self, info_tuple):
        self.tableWidget.setRowCount(len(info_tuple))

        for row, line in enumerate(info_tuple):
            for column, item in enumerate(line):
                item = unicode(item)

                if column == 6:
                    info_dict = self.sql_client.get_reverse_dict_of_table('bm_wh')
                    item = QTableWidgetItem(info_dict[item])
                elif column == 9:
                    info_dict = self.sql_client.get_reverse_dict_of_table('bm_zc')
                    item = QTableWidgetItem(info_dict[item])
                elif column == 30:
                    info_dict = self.sql_client.get_reverse_dict_of_table('bm_bm')
                    item = QTableWidgetItem(info_dict[item])
                else:
                    item = QTableWidgetItem(item)

                self.tableWidget.setItem(int(row), int(column), item)

    @pyqtSignature("")
    def on_pushButton_by_zc_clicked(self):
        """
        Slot documentation goes here.
        """
        zc_content = unicode(self.textEdit_input.toPlainText())
        # 找到对应编码
        zc_dict = self.sql_client.get_dict_of_table("bm_zc")
        try:
            zc_code = zc_dict[zc_content]
        except KeyError:
            QMessageBox.information(self, 'Message', "输入非法！", QMessageBox.Yes)
            return
        target_info = self.sql_client.get_target_info_by_zc(zc_code)
        self.fill_tableview(target_info)

# 简单介绍一下几段功能（含有额外做的加分的） 老师抽功能演示
# 周五 下午5点之前报告

    @pyqtSignature("")
    def on_pushButton_by_wh_clicked(self):
        """
        Slot documentation goes here.
        """
        wh_content = unicode(self.textEdit_input.toPlainText())
        wh_dict = self.sql_client.get_dict_of_table("bm_wh")
        try:
            wh_code = wh_dict[wh_content]
        except KeyError:
            QMessageBox.information(self, 'Message', "输入非法！", QMessageBox.Yes)
            return
        target_info = self.sql_client.get_target_info_by_wh(wh_code)
        self.fill_tableview(target_info)

    @pyqtSignature("")
    def on_pushButton_by_bm_clicked(self):
        """
        Slot documentation goes here.
        """
        bm_content = unicode(self.textEdit_input.toPlainText())
        bm_dict = self.sql_client.get_dict_of_table("bm_bm")
        try:
            bm_code = bm_dict[bm_content]
        except KeyError:
            QMessageBox.information(self, 'Message', "输入非法！", QMessageBox.Yes)
            return
        target_info = self.sql_client.get_target_info_by_bm(bm_code)
        self.fill_tableview(target_info)

