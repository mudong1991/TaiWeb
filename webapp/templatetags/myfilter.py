# -*- coding:utf-8 -*-
from django import template
from webapp.util import get_template
register = template.Library()


def shear(key, arg):
    if key:
        if len(key) > int(arg):
            return key[:int(arg)] + '...'
        else:
            return key
    else:
        return ''


# 自定义一个时间过滤器，讲月份转换成大写
# @register.filter(name='aaa')
def month_to_upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month - 1]


def app_template(key):
    template_name = get_template(key)
    return template_name


def get_file_name(key):
    return str(key.name).split('/')[-1]


# 将自定义的过滤器注册
register.filter('mouth_to_upper', month_to_upper)
register.filter('app_template', app_template)
register.filter('shear', shear)
register.filter('get_file_name', get_file_name)
