from typing import Tuple

from django.contrib import admin

from .models import EmailVerifyRecord

# Register your models here.

@admin.register(EmailVerifyRecord)
class EmailVerifyRecordAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'send_type', 'send_time')
    list_filter = ('email', 'code', 'send_type', 'send_time')
    search_fields = ('email', 'code', 'send_type', 'send_time')
