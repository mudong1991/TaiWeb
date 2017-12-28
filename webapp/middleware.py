# -*- coding:utf-8 -*-
# Created by Administrator at 2017/3/7 0007
"""
自定义中间件，对权限、请求响应做一些处理
"""
import logging
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render

# 定义一个日志器
logger = logging.getLogger('webapp.views')


class CustomExceptionMiddleWare(MiddlewareMixin):
    """
    自定义异常处理中间件
    """

    def process_exception(self, request, exception):
        """
        统一处理未捕获的异常
        :param request:
        :param exception:
        :return:
        """
        # 记录异常
        logger.error(exception.message or exception)

        return render(request, 'error_info.html', {"message": exception.message or exception, "status_code": 500},
                      status=500)

    def process_response(self, request, response):
        """
        HttpResponse重写
        :param request:
        :param response:
        :return:
        """
        #: 页面没有权限的情况处理
        if response.status_code == 403:
            return render(request, 'error_info.html', {"message": "您没有权限访问这个页面！", "status_code": 403}, status=403)
        if response.status_code == 404:
            return render(request, '404/index.html', {"message": "找不到指定页面！", "status_code": 404}, status=404)

        return response
