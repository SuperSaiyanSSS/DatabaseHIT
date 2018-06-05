# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Module implementing ProfileWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_profile import Ui_ProfileWindow

import globalvar


class ProfileWindow(QMainWindow, Ui_ProfileWindow):
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
        # 目标用户Id
        self.sql_client = globalvar.get_client()

    def set_user_id(self, user_id):
        """
        显示个人信息的入口
        """
        self.user_id = user_id
        self.show_profile()

    def show_profile(self):
        person_res, cygx_res = self.sql_client.get_profile(self.user_id)
        if person_res == ():
            response = QMessageBox.information(self, 'Message', "不存在此人！", QMessageBox.Yes)
            # return
        else:
            whcd_list = self.sql_client.get_whcd_list()
            zcbm_list = self.sql_client.get_zcbm_list()
            bmbm_list = self.sql_client.get_bmbm_list()

            self.lineEdit_zgbm.setText(unicode(person_res[0]))
            self.lineEdit_xm.setText(unicode(person_res[1]))
            xb_list = ["男", "女"]
            self.comboBox_xb.addItem(unicode(person_res[2]))
            self.comboBox_xb.addItems([xb for xb in xb_list if xb != unicode(person_res[2])])
            self.lineEdit_mz.setText(unicode(person_res[3]))
            self.lineEdit_csny.setText(unicode(person_res[4]))
            hyzk_list = ["未婚", "已婚"]
            self.comboBox_hyzk.addItem(unicode(person_res[5]))
            self.comboBox_hyzk.addItems([hyzk for hyzk in hyzk_list if hyzk != unicode(person_res[5])])
            whcd_dict = self.sql_client.get_reverse_dict_of_table("bm_wh")
            self.comboBox_whcd.addItem(whcd_dict[unicode(person_res[6])])
            self.comboBox_whcd.addItems([whcd for whcd in whcd_list if whcd != unicode(person_res[6])])
            self.lineEdit_jkzk.setText(unicode(person_res[7]))
            zzmm_list = ["党员", "预备党员", "共青团员", "群众", "民主党派"]
            self.comboBox_zzmm.addItem(unicode(person_res[8]))
            self.comboBox_zzmm.addItems([zzmm for zzmm in zzmm_list if zzmm != unicode(person_res[8])])
            zcbm_dict = self.sql_client.get_reverse_dict_of_table("bm_zc")
            self.comboBox_whcd.addItem(zcbm_dict[unicode(person_res[9])])
            self.comboBox_zcbm.addItems([zcbm for zcbm in zcbm_list if zcbm != unicode(person_res[9])])
            self.lineEdit_jg.setText(unicode(person_res[10]))
            self.lineEdit_sfzh.setText(unicode(person_res[11]))
            self.lineEdit_byxx.setText(unicode(person_res[12]))
            self.lineEdit_zytc.setText(unicode(person_res[13]))
            self.lineEdit_hkszd.setText(unicode(person_res[14]))
            hkxz_list = ["农业", "城镇"]
            self.comboBox_hkxz.addItem(unicode(person_res[15]))
            self.comboBox_hkxz.addItems([hkxz for hkxz in hkxz_list if hkxz != unicode(person_res[15])])
            self.lineEdit_xzz.setText(unicode(person_res[16]))
            self.lineEdit_zw.setText(unicode(person_res[17]))
            self.lineEdit_gzm.setText(unicode(person_res[18]))
            self.lineEdit_jspx.setText(unicode(person_res[19]))
            self.lineEdit_jlcf.setText(unicode(person_res[20]))
            self.lineEdit_smwt.setText(unicode(person_res[21]))
            self.lineEdit_tbrqm.setText(unicode(person_res[22]))
         #   self.tbrqEdit.setText(str(person_res[22]))
            self.lineEdit_tbrq.setText(unicode(person_res[23]))
            self.lineEdit_gsyj.setText(unicode(person_res[24]))
            self.lineEdit_scrq.setText(unicode(person_res[25]))
            self.lineEdit_ryxz.setText(unicode(person_res[26]))
            self.lineEdit_rcsj.setText(unicode(person_res[27]))
            self.lineEdit_ryzt.setText(unicode(person_res[28]))
            self.lineEdit_bz.setText(unicode(person_res[29]))
            bmbm_dict = self.sql_client.get_reverse_dict_of_table("bm_bm")
            self.comboBox_bmbm.addItem(bmbm_dict[unicode(person_res[30])])
            self.comboBox_bmbm.addItems([bmbm for bmbm in bmbm_list if bmbm != unicode(person_res[30])])

            if cygx_res == ():
                self.lineEdit_brgx1.setText('')
                self.lineEdit_xm1.setText('')
                self.lineEdit_hzgz1.setText('')
                self.lineEdit_brgx2.setText('')
                self.lineEdit_xm2.setText('')
                self.lineEdit_hzgz2.setText('')
            elif len(cygx_res) == 1:
                self.lineEdit_brgx1.setText(unicode(cygx_res[0][0]))
                self.lineEdit_xm1.setText(unicode(cygx_res[0][1]))
                self.lineEdit_hzgz1.setText(unicode(cygx_res[0][2]))
                self.lineEdit_brgx2.setText('')
                self.lineEdit_xm2.setText('')
                self.lineEdit_hzgz2.setText('')
            elif len(cygx_res) == 2:
                self.lineEdit_brgx1.setText(unicode(cygx_res[0][0]))
                self.lineEdit_xm1.setText(unicode(cygx_res[0][1]))
                self.lineEdit_hzgz1.setText(unicode(cygx_res[0][2]))
                self.lineEdit_brgx2.setText(unicode(cygx_res[1][0]))
                self.lineEdit_xm2.setText(unicode(cygx_res[1][1]))
                self.lineEdit_hzgz2.setText(unicode(cygx_res[1][2]))

    @pyqtSignature("")
    def on_pushButton_update_clicked(self):
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

        zc_dict = self.sql_client.get_dict_of_table("bm_zc")
        zc_key = zc_dict[zcbm]
        bm_dict = self.sql_client.get_dict_of_table("bm_bm")
        bm_key = bm_dict[bmbm]
        whcd_dict = self.sql_client.get_dict_of_table("bm_wh")
        whcd_key = whcd_dict[whcd]

      #  self.sql_client.add_person_document(zgbm, xm, xb,mz, csny, hyzk, whcd_key, jkzk,zzmm,zc_key,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,bm_key)
    
    @pyqtSignature("")
    def on_pushButton_delete_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
