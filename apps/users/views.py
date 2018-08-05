import json
import re

from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .forms import LoginFrom

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
    def get(self, request):
        print(request.COOKIES.get('sessionid'))
        print(request.session)
        print(type(request.session))

    def post(self, request):
        print(request.user)
        data = json.loads(request.body)
        login_form = LoginFrom(data)
        if login_form.is_valid():
            user = authenticate(username=data['username'], password=data['password'])
            # print(user)
            if user is not None:
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录名或登录密码不正确')
        else:
            for key, errors in login_form.errors.items():
                print(key, ':', re.split('[<li>|</li>]', str(errors))[10])
                return HttpResponse('请检查你输入的字符是否有误，用户名和密码为必填项，密码最大长度为20个字符')


class UsersView:
    @classmethod
    def login(cls):
        def view(request):
            print(request.method)
            return HttpResponse('kk')
        return view
