# -*- coding: UTF-8 -*-
__author__ = 'MD'
from django.contrib.auth.models import *
from django.contrib.auth.hashers import make_password
from webapp.models import *
import threading


def init():
    """
    初始化权限
    :return:
    """
    user_count = User.objects.count()
    if user_count > 0:
        return
    User.objects.create(username='admin', password=make_password('123456'), is_staff=True, is_active=True, is_superuser=True)


def thread_init(sender, **kwargs):
    """
        第一个参数必须是sender，且必须有kwargs参数

        :param sender:
        :param kwargs:
        :return:
        """

    # 在另一个线程中执行init方法，主要是为了解决数据库事务提交延迟的问题。
    t = threading.Timer(1, init)

    t.start()
