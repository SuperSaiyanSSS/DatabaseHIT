# -*- coding: utf-8 -*-

"""
Module implementing ManageWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

from Ui_manage import Ui_ManageWindow


class ManageWindow(QMainWindow, Ui_ManageWindow):
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
    
    @pyqtSignature("")
    def on_pushButton_table_clicked(self):
        """
        Slot documentation goes here.
        """
        from manage_table import ManageTableWindow
        self.table_window = ManageTableWindow()
        self.table_window.show()
    
    @pyqtSignature("")
    def on_pushButton_user_clicked(self):
        """
        Slot documentation goes here.
        """
        from manage_user import ManageUserWindow
        self.user_window = ManageUserWindow()
        self.user_window.show()
    
    @pyqtSignature("")
    def on_pushButton_database_clicked(self):
        """
        Slot documentation goes here.
        """
        from manage_database import ManageDatabaseWindow
        self.database_window = ManageDatabaseWindow()
        self.database_window.show()
