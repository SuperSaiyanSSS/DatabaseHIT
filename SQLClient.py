# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Module implementing SQLClient.
"""

import MySQLdb


class SQLClient(object):

    def __init__(self, user, password):
        self.db = MySQLdb.connect("localhost", "root", "123456", "hr_manage")
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

        for line in data:
            if line[0] == self.user and line[1] == self.password:
                return True
        return False

    def get_whcd_list(self):
        self.cursor.execute("SELECT * FROM bm_wh")
        data = self.cursor.fetchall()

        whcd_list = []
        for line in data:
            whcd_list.append(unicode(line[1]))
        return whcd_list




if __name__ == '__main__':
    a = SQLClient()
