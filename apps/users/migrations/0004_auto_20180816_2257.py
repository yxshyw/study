# Generated by Django 2.0.7 on 2018-08-16 22:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180806_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailverifyrecord',
            name='send_time',
        ),
        migrations.AddField(
            model_name='emailverifyrecord',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 16, 23, 2, 32, 990811), verbose_name='过期时间'),
        ),
    ]