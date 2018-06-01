# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
保存可跨文件修改的真·全局变量的文件，而不是普通的不可被多个文件修改的全局变量
"""
import sys
import SQLClient


def _init(user, password):
    global sql_client
    sql_client = SQLClient.SQLClient(user, password)
    return sql_client

def get_client():
    global sql_client
    return sql_client