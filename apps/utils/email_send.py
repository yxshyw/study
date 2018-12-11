# __author__ = 'yxshyw'
# __date__ = '2018/8/9 21:47'

import random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from study.settings import EMAIL_FROM


# noinspection PyArgumentList
def send_register_email(email, send_type='register'):
    s = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'
    code = ''
    for i in range(16):
        code += s[random.randint(0, len(s)-1)]
    if send_type == 'register':
        email_title = '注册标题'
        email_body = '注册内容：http://127.0.0.1:8000/users/active/{0}/'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            EmailVerifyRecord.objects.create(
                code=code,
                email=email,
                send_type=send_type
            )
    elif send_type == 'forget':
        email_title = '重置密码'
        email_body = '注册内容：http://127.0.0.1:8000/users/reset/{0}/'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            EmailVerifyRecord.objects.create(
                code=code,
                email=email,
                send_type=send_type
            )

