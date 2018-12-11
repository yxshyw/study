import json
import re
from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.sessions.models import Session

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginFrom, RegisterForm, LoginFromSet
from utils.email_send import send_register_email

# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print('异常信息:', e)
            return None


class LoginView(View):
    def post(self, request):
        print(self.request.user)
        data = json.loads(self.request.body)
        login_form = LoginFrom(data)
        if login_form.is_valid():
            user = authenticate(username=data['username'], password=data['password'])
            # print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('登录成功')
                else:
                    return HttpResponse('该用户未激活')
            else:
                return HttpResponse('登录名或登录密码错误')
        else:
            print(login_form.errors)
            print(login_form.errors.as_data())
            for key, errors in login_form.errors.items():
                # print(key, ':', re.split('[<li>|</li>]', str(errors))[10])
                return HttpResponse(login_form.errors.as_text())


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        data = json.loads(self.request.body)
        register_form = RegisterForm(data)
        if UserProfile.objects.filter(email=data['email']):
            return HttpResponse('email 已存在')
        if register_form.is_valid():
            try:
                UserProfile.objects.create(
                    email=data['email'],
                    username=data['email'],
                    password=make_password(data['password']),
                    is_active=False
                )
                send_register_email(data['email'])
            except Exception as e:
                print('异常信息:', e)
            return HttpResponse('yes')
        else:
            return HttpResponse('no')


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
            return HttpResponse('激活成功')
        else:
            return HttpResponse('链接有误')


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.set_password('123456')
                user.save()
            return HttpResponse('重置密码成功')
        else:
            return HttpResponse('链接有误')


class ForgetPwdView(View):
    def get(self, request):
        pass

    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        send_register_email(email, 'forget')
        return HttpResponse('发送成功')


class UsersView:
    @classmethod
    def login(cls):
        def view(request):
            print(request.method)
            return HttpResponse('kk')
        return view
