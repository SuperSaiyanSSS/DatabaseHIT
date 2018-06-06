# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing ManageDatabaseWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui

from Ui_manage_database import Ui_ManageDatabaseWindow
import globalvar


class ManageDatabaseWindow(QMainWindow, Ui_ManageDatabaseWindow):
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
    
    @pyqtSignature("")
    def on_pushButton_beifen_clicked(self):
        """
        Slot documentation goes here.
        """
        name = unicode(self.lineEdit_beifen.text())
        self.sql_client.beifen(name)
        QtGui.QMessageBox.information(self, 'Message', "备份成功！", QtGui.QMessageBox.Yes)


    @pyqtSignature("")
    def on_pushButton_huifu_clicked(self):
        """
        Slot documentation goes here.
        """
        name = unicode(self.lineEdit_huifu.text())
        self.sql_client.huifu(name)
        QtGui.QMessageBox.information(self, 'Message', "恢复成功！", QtGui.QMessageBox.Yes)
