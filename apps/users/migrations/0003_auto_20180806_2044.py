# Generated by Django 2.0.7 on 2018-08-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180728_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], default='register', max_length=10, verbose_name='验证码类型'),
        ),
    ]
