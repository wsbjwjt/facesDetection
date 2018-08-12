# -*- coding:utf-8 -*-
__author__ = 'Eric'
__date__ = '2018/8/11 16:52'

import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    list_display = ['id', 'code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)