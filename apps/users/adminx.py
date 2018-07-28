# __author__ = 'yxshyw'
# __date__ = '2018/7/28 17:12'

from .models import EmailVerifyRecord, PageBanner
import xadmin

class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
