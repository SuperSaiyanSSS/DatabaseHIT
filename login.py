# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing DialogLogin.
"""
import sys

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_login import Ui_DialogLogin
from SQLClient import SQLClient
import globalvar



class DialogLogin(QDialog, Ui_DialogLogin):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructors
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.main_window = None

    @pyqtSignature("")
    def on_pushButton_login_clicked(self):
        """
        Slot documentation goes here.
        """

        username = unicode(self.lineEdit_user.text())
        password = unicode(self.lineEdit_password.text())

        # 创建SQL客户端。保证全局可用。
        global sql_client
        sql_client = globalvar._init(username, password)
        if sql_client.check_user():
            print "登陆成功"
            from main import MainWindow
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            print "用户名或密码错误！"


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = DialogLogin()
    dlg.show()
    sys.exit(app.exec_())
