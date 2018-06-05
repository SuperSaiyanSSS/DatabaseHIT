# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing BrowseWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_browse import Ui_BrowseWindow
import globalvar

class BrowseWindow(QMainWindow, Ui_BrowseWindow):
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

        self.init_tableview()


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

    def init_tableview(self):

        data = self.sql_client.init_tableview()

        # 设置行数
        self.tableWidget.setRowCount(len(data))

        for row, line in enumerate(data):
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
    def on_pushButton_find_id_accurately_clicked(self):
        """
        Slot documentation goes here.
        """
        user_id = self.textEdit_find.toPlainText()
        data = self.sql_client.get_info_by_id_accurately(user_id)
        self.fill_tableview(data)


    @pyqtSignature("")
    def on_pushButton_find_id_vaguely_clicked(self):
        """
        Slot documentation goes here.
        """
        user_id = self.textEdit_find.toPlainText()
        data = self.sql_client.get_info_by_id_vaguely(user_id)
        self.fill_tableview(data)
    
    @pyqtSignature("")
    def on_pushButton_find_name_accurately_clicked(self):
        """
        Slot documentation goes here.
        """
        user_name = self.textEdit_find.toPlainText()
        data = self.sql_client.get_info_by_name_accurately(user_name)
        self.fill_tableview(data)

    
    @pyqtSignature("")
    def on_pushButton_find_name_vaguely_clicked(self):
        """
        Slot documentation goes here.
        """
        user_name = self.textEdit_find.toPlainText()
        data = self.sql_client.get_info_by_name_vaguely(user_name)
        self.fill_tableview(data)

    @staticmethod
    def chinese_to_code(chinese):

        SQL_column_name = ['zgbm', 'xm', 'xb', 'mz', 'csny', 'hyzk', 'whcd', 'jkzk', 'zzmm', 'zcbm', 'jg', 'sfzh',
                           'byxx', 'zytc', 'hkszd', 'hkxz', 'xzz', 'zw', 'gzm', 'jspx', 'jlcf', 'smwt', 'tbrqm', 'tbrq',
                           'gsyj', 'scrq', 'ryxz', 'rcsj', 'ryzt', 'bz', 'bmbm']

        column_name = ['职工编码', '姓名', '性别', '民族', '出生年月', '婚姻状况', '文化程度', '健康状况', '政治面貌', '职称', '籍贯', '身份证号码', '毕业学校',
                       '专业或特长', '户口所在地', '户口性质', '现住址', '职务', '工种名', '何时技术培训', '何时奖励和处分', '需要说明问题', '填表人签名', '填表日期',
                       '公司审查意见', '审查日期', '人员性质', '入厂时间', '人员状态', '备注', '部门']
        dict_Map = {}
        for i in range(len(column_name)):
            dict_Map[column_name[i]] = SQL_column_name[i]

        return dict_Map[chinese]

    @pyqtSignature("")
    def on_pushButton_update_clicked(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget.currentIndex().row()
        column = self.tableWidget.currentIndex().column()

        column_name = unicode(self.tableWidget.horizontalHeaderItem(column).text())# 获取列名
        print column_name
        column_name = self.chinese_to_code(column_name)
        # 找到对于行的第一项（职工编码项）
        zgbm = unicode(self.tableWidget.takeItem(row, 0).text())
        self.tableWidget.setItem(row, 0, QTableWidgetItem(zgbm))
        update_content = self.textEdit_find.toPlainText()
        Qupdate_content = QTableWidgetItem(update_content)
        self.tableWidget.setItem(row, column, Qupdate_content)

        result_signal = self.sql_client.update_profile(zgbm, column_name, update_content)
        if result_signal:
            QMessageBox.information(self, 'Message', "修改成功！", QMessageBox.Yes)
        else:
            QMessageBox.information(self, 'Message', "修改失败！", QMessageBox.Yes)
    
    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        row = self.tableWidget.currentIndex().row()
        # 找到对于行的第一项（职工编码项）
        zgbm = unicode(self.tableWidget.takeItem(row, 0).text())
        self.tableWidget.setItem(row, 0, QTableWidgetItem(zgbm))
        result_signal = self.sql_client.delete_profile(zgbm)
        if result_signal:
            QMessageBox.information(self, 'Message', "删除成功！", QMessageBox.Yes)
            self.tableWidget.removeRow(row)
        else:
            QMessageBox.information(self, 'Message', "删除失败 难受啊马飞飞！", QMessageBox.Yes)


    @pyqtSignature("")
    def on_pushButton_view_person_clicked(self):
        """
        Slot documentation goes here.
        """
        user_id = self.textEdit_id.toPlainText()
        from profile import ProfileWindow
        self.profile_window = ProfileWindow()
        self.profile_window.set_user_id(user_id)
        self.profile_window.show()
        pass
