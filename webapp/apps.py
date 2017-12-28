# -*- coding: utf-8 -*-
"""
解决初始化权限问题，在migrate完成后执行一个方法
需要在__init__模块中添加default_app_config = 'firstapp.apps.MyAppConfig'
"""
__author__ = 'MD'
from django.db.models.signals import post_migrate
from django.apps import AppConfig


class WebappConfig(AppConfig):
    name = 'webapp'

    def ready(self):
        from webapp.init_data import thread_init  # 最好是在ready方法内再引入models.py
        post_migrate.connect(receiver=thread_init, sender=self)
