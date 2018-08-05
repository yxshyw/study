# __author__ = 'yxshyw'
# __date__ = '2018/8/5 10:32'

from django import forms

class LoginFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=20)



