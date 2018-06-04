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
        self.comboBox_whcd.addItems(sql_client.get_whcd_list())
        self.comboBox_zcbm.addItems(sql_client.get_zcbm_list())
        self.comboBox_bmbm.addItems(sql_client.get_bmbm_list())


    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        zgbm = unicode(self.lineEdit_zgbm.text())
        xm = unicode(self.lineEdit_xm.text())
        xb = unicode(self.comboBox_xb.currentText())
        mz = unicode(self.lineEdit_mz.text())
        csny = unicode(self.lineEdit_csny.text())
        hyzk = unicode(self.comboBox_hyzk.currentText())
        whcd = unicode(self.comboBox_whcd.currentText())
        jkzk = unicode(self.lineEdit_jkzk.text())
        zzmm = unicode(self.comboBox_zzmm.currentText())
        zcbm = unicode(self.comboBox_zcbm.currentText())
        jg = unicode(self.lineEdit_jg.text())
        sfzh = unicode(self.lineEdit_sfzh.text())
        byxx = unicode(self.lineEdit_byxx.text())
        zytc = unicode(self.lineEdit_zytc.text())
        hkszd = unicode(self.lineEdit_hkszd.text())
        hkxz = unicode(self.comboBox_hkxz.currentText())
        xzz = unicode(self.lineEdit_xzz.text())
        zw = unicode(self.lineEdit_zw.text())
        gzm = unicode(self.lineEdit_gzm.text())
        jspx = unicode(self.lineEdit_jspx.text())
        jlcf = unicode(self.lineEdit_jlcf.text())
        smwt = unicode(self.lineEdit_smwt.text())
        tbrqm = unicode(self.lineEdit_tbrqm.text())
        tbrq = unicode(self.lineEdit_tbrq.text())
        gsyj = unicode(self.lineEdit_gsyj.text())
        scrq = unicode(self.lineEdit_scrq.text())
        ryxz = unicode(self.lineEdit_ryxz.text())
        rcsj = unicode(self.lineEdit_rcsj.text())
        ryzt = unicode(self.lineEdit_ryzt.text())
        bz = unicode(self.lineEdit_bz.text())
        bmbm = unicode(self.comboBox_bmbm.currentText())

        xm1 = unicode(self.lineEdit_xm1.text())
        xm2 = unicode(self.lineEdit_xm2.text())
        brgx1 = unicode(self.lineEdit_brgx1.text())
        brgx2 = unicode(self.lineEdit_brgx2.text())
        hzgz1 = unicode(self.lineEdit_hzgz1.text())
        hzgz2 = unicode(self.lineEdit_hzgz2.text())

        sql_client = globalvar.get_client()
        zc_dict = sql_client.get_dict_of_table("bm_zc")
        zc_key = zc_dict[zcbm]
        bm_dict = sql_client.get_dict_of_table("bm_bm")
        bm_key = bm_dict[bmbm]
        whcd_dict = sql_client.get_dict_of_table("bm_wh")
        whcd_key = whcd_dict[whcd]

        sql_client.add_person_document(zgbm, xm, xb,mz, csny, hyzk, whcd_key, jkzk,zzmm,zc_key,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,bm_key)

        print unicode(self.comboBox_xb.currentText())
       # print unicode(self.comboBox_xb.itemText(1))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = AddWindow()
    dlg.show()
    sys.exit(app.exec_())