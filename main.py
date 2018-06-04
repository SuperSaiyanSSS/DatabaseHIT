# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
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
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        from add import AddWindow
        self.add_window = AddWindow()
        self.add_window.show()

    @pyqtSignature("")
    def on_pushButton_view_clicked(self):
        """
        Slot documentation goes here.
        """
        from browse import BrowseWindow
        self.browse_window = BrowseWindow()
        self.browse_window.show()
    
    @pyqtSignature("")
    def on_pushButton_analyse_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_manage_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
