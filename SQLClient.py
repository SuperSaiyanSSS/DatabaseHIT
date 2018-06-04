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

    def add_person_document(self, zgbm, xm, xb, mz, csny, hyzk, whcd, jkzk, zzmm, zc, jg, sfzh, byxx, zytc, hkszd, hkxz, xzz, zw, gzm,
                   jspx, jlcf, smwt, tbrqm, tbrq, gsyj, scrq, ryxz, rcsj, ryzt, bz, szbm):
        sqlstr = "INSERT INTO m_dadj(zgbm,xm, xb,mz,csny,hyzk,whcd, jkzk,zzmm,zcbm,jg,sfzh,byxx,zytc,hkszd,hkxz,xzz,zw,gzm,jspx,jlcf,smwt,tbrqm,tbrq,gsyj,scrq,ryxz,rcsj,ryzt,bz,bmbm) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (
        zgbm, xm, xb, mz, csny, hyzk, whcd, jkzk, zzmm, zc, jg, sfzh, byxx, zytc, hkszd, hkxz, xzz, zw, gzm, jspx, jlcf,
        smwt, tbrqm, tbrq, gsyj, scrq, ryxz, rcsj, ryzt, bz, szbm)

        print sqlstr
        try:
            self.cursor.execute(sqlstr)
            self.db.commit()
            print '插入成功！'
            return True
        except Exception, e:
            print e
            return False

    def get_dict_of_table(self, table_name):
        """
        获取dict形式的编码表
        :param table_name: 表名
        :return: {名称1：对应编码1, 名称2：对应编码2, ...}
        """
        self.cursor.execute("SELECT * FROM %s" %table_name)
        data = self.cursor.fetchall()
        table_dict = {}
        for line in data:
            table_dict[line[1]] = line[0]
        return table_dict

    def init_tableview(self):
        self.cursor.execute("SELECT * FROM m_dadj")
        data = self.cursor.fetchall()
        print type(data)
        # table_list = []
        # for i in data:
        #     table_list.append(i)
        #     print type(i[0])
        return data

    def get_info_by_id_accurately(self, id):
        self.cursor.execute("SELECT * FROM m_dadj WHERE zgbm = %s" % id)
        data = self.cursor.fetchall()
        return data

    def get_info_by_id_vaguely(self, id):
        self.cursor.execute("SELECT * FROM m_dadj WHERE zgbm LIKE '%%%s%%'" % id)
        data = self.cursor.fetchall()
        return data

    def get_info_by_name_accurately(self, name):
        self.cursor.execute("SELECT * FROM m_dadj WHERE xm ='%s'" % name)
        data = self.cursor.fetchall()
        return data

    def get_info_by_name_vaguely(self, name):
        self.cursor.execute("SELECT * FROM m_dadj WHERE xm LIKE '%%%s%%'" % name)
        data = self.cursor.fetchall()
        return data



if __name__ == '__main__':
    a = SQLClient()
