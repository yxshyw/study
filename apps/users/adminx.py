# __author__ = 'yxshyw'
# __date__ = '2018/7/28 17:12'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, PageBanner

# class BaseSetting:
#     enable_themes = True
#     use_bootswatch = True


class GlobalSetting:
    site_title = 'yxshywtitle'
    site_footer = 'yxshywfoot'
    menu_style = 'accordion'

class EmailVerifyRecordAdmin:
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']

class PageBannerAdmin:
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(PageBanner, PageBannerAdmin)

# xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

