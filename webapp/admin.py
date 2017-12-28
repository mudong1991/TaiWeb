# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from webapp.models import *
from django.conf import settings
from django.contrib.auth.models import User, Group


class MyAdminSite(admin.AdminSite):
    site_title = settings.ADMIN_TITLE
    site_header = settings.ADMIN_HEADER


# 文章模型admin显示管理
class KindeAdmin(admin.ModelAdmin):

    # 引入媒体文件，创建富文本
    class Media:
        js = (
            '/static/scripts/kindeditor-4.1.10/kindeditor-min.js',
            '/static/scripts/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/scripts/kindeditor-4.1.10/config.js',
        )


class ProductAdmin(KindeAdmin):
    list_display = ('name', 'description', 'show_index')
    list_editable = ('show_index', )


class NewsAdmin(KindeAdmin):
    list_display = ('title', 'show_index')
    list_editable = ('show_index',)


class ApplicationAdmin(KindeAdmin):
    list_display = ('name', 'description', 'show_index')
    list_editable = ('show_index',)


class DevelopHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time')
    list_editable = ('date_time',)


class SiteMessageAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'phone_num', 'content')

# Register your models here.
admin_site = MyAdminSite(name='admin')
admin_site.register(User)
admin_site.register(Group)
admin_site.register(Ad)
admin_site.register(CompanyVideo)
admin_site.register(Product, ProductAdmin)
admin_site.register(ProductCategory, KindeAdmin)
admin_site.register(News, NewsAdmin)
# 关于我们
admin_site.register(CompanyIntro, KindeAdmin)
admin_site.register(CompanyCulture, KindeAdmin)
admin_site.register(CompanyStructure, KindeAdmin)
admin_site.register(DevelopHistory, DevelopHistoryAdmin)
# 联系我们
admin_site.register(ContactList)
admin_site.register(SiteMessage, SiteMessageAdmin)
admin_site.register(Recruit, KindeAdmin)
# 服务项目
admin_site.register(Service, KindeAdmin)
# 应用案例
admin_site.register(ApplicationCase, ApplicationAdmin)
