# Generated by Django 2.0.7 on 2018-08-21 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180816_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 21, 7, 24, 15, 398720), verbose_name='过期时间'),
        ),
    ]