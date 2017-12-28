# -*- coding:utf-8 -*-
# file: util
# author: Mundy
# date: 2017/7/31 0031
"""
webapp工具方法
"""


def get_template(name):
    """
    :param name: 网页模板名
    :return: 网页模板(绝对路径)
    """
    if name.endswith('html'):
        return "webapp/" + name
    else:
        return 'webapp/' + name + '.html'