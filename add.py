# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing AddWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_add import Ui_MainWindow

import globalvar



class AddWindow(QMainWindow, Ui_MainWindow):
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
        self.comboBox_xb.addItems(["男", "女"])
        self.comboBox_hyzk.addItems(["未婚", "已婚"])
        self.comboBox_zzmm.addItems(["党员", "预备党员", "共青团员", "群众", "民主党派"])
        self.comboBox_hkxz.addItems(["农业", "非农业"])
        self.linkage_combox()

    def linkage_combox(self):
        """
        实现下拉框与部门表、职称表、文化程度表的联动
        :return: None
        """
        sql_client = globalvar.get_client()
        for i in sql_client.get_whcd_list():
            print i
        self.comboBox_whcd.addItems(sql_client.get_whcd_list())


    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        print 777

        print unicode(self.comboBox_xb.currentText())
       # print unicode(self.comboBox_xb.itemText(1))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = AddWindow()
    dlg.show()
    sys.exit(app.exec_())