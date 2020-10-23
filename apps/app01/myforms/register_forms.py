from django import forms
from app01 import models


# 注册form组件
class RegForm(forms.Form):
    username = forms.CharField(max_length=16, min_length=8, label='用户名',
                               error_messages={'required': '用户名不能为空', 'max_length': '用户名长度8-16位',
                                               'min_length': '用户名长度8-16位'},
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(max_length=8, min_length=8, label='密码',
                               error_messages={'required': '密码不能为空', 'max_length': '密码长度为8位',
                                               'min_length': '密码长度为8位'},
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    re_password = forms.CharField(max_length=8, min_length=8, label='确认密码',
                                  error_messages={'required': '两次密码不一致', 'max_length': '两次密码不一致',
                                                  'min_length': '两次密码不一致'},
                                  widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="邮箱", error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式不正确'},
                             widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user_obj = models.UserInfo.objects.filter(username=username).first()
        if user_obj:
            self.add_error("username", '用户名已存在')
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if not password == re_password:
            self.add_error('re_password', '两次密码不一致')
        return self.cleaned_data
