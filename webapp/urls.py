# -*-coding:utf-8 -*-
from django.conf.urls import url
from webapp.views import *

urlpatterns = [
    # 首页
    url(r'^$', index, name='index'),
    url(r'^search/$', search, name='search'),
    # 服务项目
    url(r'^service/$', service, name='service'),
    # 产品
    url(r'^product_category/$', product_category, name='product_category'),
    url(r'^product/$', product, name='product'),
    # 关于我们
    url(r'^about_us/$', about_us, name='about_us'),
    url(r'^about_us/company_intro/$', company_intro, name='company_intro'),
    url(r'^about_us/develop_history/$', develop_history, name='develop_history'),
    url(r'^about_us/culture/$', culture, name='culture'),
    url(r'^about_us/structure/$', structure, name='structure'),
    url(r'^about_us/news/$', news, name='news'),
    url(r'^news/thumbs/$', news_thumbs, name='news_thumbs'),
    # 应用案例
    url(r'^application/$', application, name='application'),
    # 联系我们
    url(r'^contact_us/$', contact_us, name='contact_us'),
    url(r'^contact_us/contact_kinds/$', contact_kinds, name='contact_kinds'),
    url(r'^contact_us/recruit/$', recruit, name='recruit'),
    # 文件下载
    # url(r'download/', download, name='download')
]
