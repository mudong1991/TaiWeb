# -*- coding:utf-8 -*-
"""TaiWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import settings
from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from webapp.upload import upload_image
from webapp.admin import admin_site

urlpatterns = [
    url(r'^', include('webapp.urls')),

    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin_site.urls)),

    # 静态文件映射地址设置
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # 媒体文件映射地址设置
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # kindeditor上传文件路径
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
]
