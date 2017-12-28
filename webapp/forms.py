# -*-coding:utf-8-*-
# __author__ = 'MD'
from __future__ import unicode_literals
from django import forms


class MessageForm(forms.Form):
    """
    留言表单
    """
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'id': 'username', 'class': 'form-control', 'required': 'required', 'name': 'username',
                                                               'placeholder': '您的姓名', 'tabindex': '1', }),
                                error_messages={'required': '姓名不能为空'}, max_length=50)
    email = forms.EmailField(label='邮箱', widget=forms.TextInput(attrs={'id': 'email',  'placeholder': '邮箱地址', 'required': 'required', 'tabindex': '2', 'name': 'email',
                                                           'email': True, 'invalid': 'invalid', 'class': 'form-control', "pattern": "^([0-9A-Za-z\-_\.]+)@([0-9a-z]+\.[a-z]{2,3}(\.[a-z]{2})?)$"}),
                             max_length=200, error_messages={'required': '邮箱不能为空'})
    phone_num = forms.CharField(label='手机 ', widget=forms.TextInput(attrs={'id': 'phone',  'placeholder': '手机号', 'tabindex': '3', 'class': 'form-control', 'name': 'phone_num'}),
                                max_length=20, required=False)
    content = forms.CharField(label='内容', widget=forms.Textarea(attrs={'id': 'content', 'class': 'form-control', 'required': 'required',  'name': 'content',
                                                           'placeholder': '说点什么吧', 'tabindex': '4'}),
                              error_messages={'required': '留言内容不能为空'}, max_length=2000)