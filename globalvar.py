# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
保存可跨文件修改的真·全局变量的文件，而不是普通的不可被多个文件修改的全局变量
"""
import sys
import SQLClient
reload(sys)
sys.setdefaultencoding('utf-8')

def _init(user, password):
    global sql_client
    sql_client = SQLClient.SQLClient(user, password)
    return sql_client

def get_client():
    global sql_client
    return sql_client


key = 0xff


def encrypt(src):
    return ''.join([unichr(ord(x)^key) for x in src]).encode('utf-8').upper()


def decrypt(src):
    return ''.join([unichr(ord(x)^key) for x in src.decode('utf-8')])

if __name__ == '__main__':
    list_ = ['540845199705184854', '847578199711265846', '370954199711054879', '263589622522336522', '6545236653314556', '4648794654897994', '565646118797615459', '565484615613879', '625148216548415', '37098319930304591', '845478199703035687']
    for i in list_:
        print encrypt(i)