# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing ManageUserWindow.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

from Ui_manage_user import Ui_ManageUserWindow
import globalvar


class ManageUserWindow(QMainWindow, Ui_ManageUserWindow):
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
        self.lineEdit_last.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_new1.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_new2.setEchoMode(QtGui.QLineEdit.Password)
        self.sql_client = globalvar.get_client()

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        last = unicode(self.lineEdit_last.text())
        new1 = unicode(self.lineEdit_new1.text())
        new2 = unicode(self.lineEdit_new2.text())
        if new1 != new2:
            QtGui.QMessageBox.information(self, 'Message', "两次密码输入不一致！", QtGui.QMessageBox.Yes)
        test_sql_client = globalvar._init(self.sql_client.user, last)
        if test_sql_client.check_user():
            self.sql_client.update_admin_password(new2)
            globalvar._init(self.sql_client.user, new2)
            QtGui.QMessageBox.information(self, 'Message', "修改成功！", QtGui.QMessageBox.Yes)
        else:
            QtGui.QMessageBox.information(self, 'Message', "旧密码输入错误！", QtGui.QMessageBox.Yes)