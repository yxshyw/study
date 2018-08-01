import json

from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile

# Create your views here.
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None

def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=data['username'], password=data['password'])
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录名或登录密码不正确')
    else:
        return HttpResponse('你的请求方式不允许')


class UsersView:
    @classmethod
    def login(cls):
        def view(request):
            print(request.method)
            return HttpResponse('kk')
        return view
