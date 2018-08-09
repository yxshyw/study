# __author__ = 'yxshyw'
# __date__ = '2018/8/5 10:32'

from django import forms
from captcha.fields import CaptchaField

class LoginFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=20)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=20)
    # captcha = CaptchaField()

