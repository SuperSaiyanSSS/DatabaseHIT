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
                print item
                item = QTableWidgetItem(item)
                self.tableWidget.setItem(int(row), int(column), item)

    def init_tableview(self):

        data = self.sql_client.init_tableview()

        # 设置行数
        self.tableWidget.setRowCount(len(data))

        for row, line in enumerate(data):
            for column, item in enumerate(line):
                item = unicode(item)
                print item
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


    @pyqtSignature("")
    def on_pushButton_update_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_view_person_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
