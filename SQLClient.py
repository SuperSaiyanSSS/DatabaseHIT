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

        #return True
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

    def get_reverse_dict_of_table(self, table_name):
        """
        获取dict形式的编码表
        :param table_name: 表名
        :return: {对应编码1: 名称1, 对应编码2：名称2, ...}
        """
        self.cursor.execute("SELECT * FROM %s" % table_name)
        data = self.cursor.fetchall()
        table_dict = {}
        for line in data:
            table_dict[line[0]] = line[1]
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

    # 个人档案查询
    def get_profile(self, user_id):
        sqlstr = "SELECT * FROM m_dadj WHERE zgbm = %s" % user_id
        print "???" + sqlstr
        person_count = self.cursor.execute(sqlstr)
        if person_count != 0:
            person_res = self.cursor.fetchone()
        else:
            person_res = ()
        sqlstr = "SELECT brgx,xm,job FROM cygx WHERE zgbm = %s" % user_id
        cygx_count = self.cursor.execute(sqlstr)
        if cygx_count != 0:
            cygx_res = self.cursor.fetchall()
        else:
            cygx_res = ()
        # print person_res, cygx_res
        return person_res, cygx_res

    def get_target_info_by_zc(self, zc):
        test_count = self.cursor.execute("SELECT * FROM m_dadj WHERE zcbm ='%s'" % zc)
        if test_count == 0:
            return ()
        data = self.cursor.fetchall()
        return data

    def get_target_info_by_wh(self, wh):
        test_count = self.cursor.execute("SELECT * FROM m_dadj WHERE whcd ='%s'" % wh)
        if test_count == 0:
            return ()
        data = self.cursor.fetchall()
        return data

    def get_target_info_by_bm(self, bm):
        test_count = self.cursor.execute("SELECT * FROM m_dadj WHERE bmbm ='%s'" % bm)
        if test_count == 0:
            return ()
        data = self.cursor.fetchall()
        return data

    # 更新个人信息
    def update_profile(self, zgbm, column_name, update_content):
        update_content = unicode(update_content)

        if column_name == 'zcbm' or column_name == 'bmbm'or column_name == 'whcd':
            info_dict = self.get_dict_of_table('bm_'+column_name[:2])
            update_content = info_dict[update_content]

        try:
            sqlstr = "UPDATE m_dadj SET %s = '%s' WHERE zgbm = %s" % (column_name, update_content, zgbm)
            # print sqlstr
            self.cursor.execute(sqlstr)
            self.db.commit()
            print '修改成功！ '
            return True
        except Exception, e:
            print e
            return False

    # 删除个人信息
    def delete_profile(self, user_id):
        try:
            self.cursor.execute("DELETE FROM m_dadj WHERE zgbm = %s" % user_id)
            self.db.commit()
            return True
        except Exception as e:
            print e
            return False

    # 获取公司总人数
    def count_sum_people(self):
        self.cursor.execute("SELECT COUNT(*) FROM m_dadj")
        count = self.cursor.fetchall()
        print count[0][0]
        return count[0][0]

    # 获取职称表信息
    def get_zc_info(self):
        self.cursor.execute("SELECT * FROM bm_zc")
        data = self.cursor.fetchall()
        return data

    # 获取文化表信息
    def get_wh_info(self):
        self.cursor.execute("SELECT * FROM bm_wh")
        data = self.cursor.fetchall()
        return data

    # 获取部门表信息
    def get_bm_info(self):
        self.cursor.execute("SELECT * FROM bm_bm")
        data = self.cursor.fetchall()
        return data

    # 增加职程表信息
    def add_zc_info(self, code, name):
        self.cursor.execute("INSERT INTO bm_zc(zcbm, zcmc) VALUES('%s', '%s')" % (code, name))
        self.db.commit()

    # 增加文化表信息
    def add_wh_info(self, code, name):
        self.cursor.execute("INSERT INTO bm_wh(whbm, whcd) VALUES('%s', '%s')" % (code, name))
        self.db.commit()

    # 增加部门表信息
    def add_bm_info(self, code, name):
        self.cursor.execute("INSERT INTO bm_bm(bmbm, bmm) VALUES('%s', '%s')" % (code, name))
        self.db.commit()

    # 删除职称表信息
    def delete_zc_info(self, xxbm):
        self.cursor.execute("DELETE FROM bm_zc WHERE zcbm = '%s'" % xxbm)
        self.db.commit()

    # 删除文化表信息
    def delete_wh_info(self, xxbm):
        self.cursor.execute("DELETE FROM bm_wh WHERE whbm = '%s'" % xxbm)
        self.db.commit()

    # 删除部门表信息
    def delete_bm_info(self, xxbm):
        self.cursor.execute("DELETE FROM bm_bm WHERE bmbm = '%s'" % xxbm)
        self.db.commit()

    # 修改管理员密码
    def update_admin_password(self, password):
        self.cursor.execute("UPDATE admin_table SET password = '%s' WHERE user = 'admin'" % password)
        self.db.commit()

    # 数据库备份
    def beifen(self, filename):
        import os
        try:
            command = "mysqldump -uroot -p123456 HR_Manage > H:/" + filename + ".sql"
            os.system(command)
            print "备份成功 nice马飞"
            return True
        except Exception, e:
            print e
            return False

    # 数据库恢复
    def huifu(self, filename):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!必须先关闭！否则卡死
        self.db.close()
        import os
        try:
            command = "mysql -uroot -p123456 HR_Manage < H:/" + filename + ".sql"
            os.system(command)
            self.db = MySQLdb.connect("localhost", "root", "123456", "hr_manage", charset="utf8")
            self.cursor = self.db.cursor()
            return True
        except Exception, e:
            print e
            return False


if __name__ == '__main__':
    a = SQLClient()
