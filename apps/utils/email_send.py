# __author__ = 'yxshyw'
# __date__ = '2018/8/9 21:47'

import random
from users.models import EmailVerifyRecord

def send_register_email(email, send_type='register'):
    code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    EmailVerifyRecord.objects.create(
        code=code,
        email=email,
        send_type=send_type
    )

    email_title = '忘记密码标题'
    email_body = '忘记密码内容'
    if send_type == 'register':
        email_title = '注册标题'
        email_body = '注册内容：http://127.0.0.1:8000/users/active/{0}'.format(code)

