# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing SQLClient.
"""

import MySQLdb


class SQLClient(object):

    def __init__(self, user, password):
        self.db = MySQLdb.connect("localhost", "root", "123456", "hr_manage", charset="utf8")
        self.cursor = self.db.cursor()

        self.cursor.execute("SELECT VERSION()")
        data = self.cursor.fetchone()
        print "Database version : %s " % data

        self.user = user
        self.password = password

    def hehe(self):
        print "777"

    def check_user(self):
        self.cursor.execute("SELECT * FROM admin_table")
        data = self.cursor.fetchall()

        return True
        for line in data:
            if line[0] == self.user and line[1] == self.password:
                return True
        return False

    def get_whcd_list(self):
        """
        获取文化程度表的名称列
        :return: whcd_list
        """
        self.cursor.execute("SELECT * FROM bm_wh")
        data = self.cursor.fetchall()

        whcd_list = []
        for line in data:
            whcd_list.append(unicode(line[1]))
        return whcd_list

    def get_zcbm_list(self):
        """
        获取职称编码表的名称列
        :return: zcbm_list
        """
        self.cursor.execute("SELECT * FROM bm_zc")
        data = self.cursor.fetchall()
        zcbm_list = []
        for line in data:
            zcbm_list.append(unicode(line[1]))
        return zcbm_list

    def get_bmbm_list(self):
        """
        获取部门编码表的名称列
        :return: bmbm_list
        """
        self.cursor.execute("SELECT * FROM bm_bm")
        data = self.cursor.fetchall()
        bmbm_list = []
        for line in data:
            bmbm_list.append(unicode(line[1]))
        return bmbm_list





if __name__ == '__main__':
    a = SQLClient()
