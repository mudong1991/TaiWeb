# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Create your models here.
# 广告（轮播）
class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    description = models.CharField(max_length=200, verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='连接地址')
    date_publish = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    order = models.IntegerField(default=9, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '轮播广告'
        verbose_name_plural = verbose_name
        db_table = "ad"
        ordering = ['order', 'id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class CompanyIntro(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    order = models.IntegerField(default=9, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '关于我们-公司简介'
        verbose_name_plural = verbose_name
        db_table = "company_intro"
        ordering = ['order', 'id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class CompanyCulture(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    order = models.IntegerField(default=9, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '关于我们-公司文化'
        verbose_name_plural = verbose_name
        db_table = "company_culture"
        ordering = ['order', 'id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class CompanyStructure(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    order = models.IntegerField(default=9, verbose_name='排列顺序(从小到大)')

    class Meta:
        verbose_name = '关于我们-组织架构'
        verbose_name_plural = verbose_name
        db_table = "company_structure"
        ordering = ['order', 'id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class DevelopHistory(models.Model):
    title = models.CharField(max_length=255, verbose_name='标题')
    content = models.CharField(max_length=2000, blank=True, null=True, verbose_name='内容')
    date_time = models.DateField(default=timezone.now, verbose_name='时间')

    class Meta:
        verbose_name = '关于我们-发展历程'
        verbose_name_plural = verbose_name
        db_table = "develop_history"
        ordering = ['date_time']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class CompanyVideo(models.Model):
    title = models.CharField(max_length=50, verbose_name='视屏标题')
    video_img = models.ImageField(upload_to='video_img/%Y/%m', verbose_name='视屏图片')
    url = models.CharField(max_length=500, verbose_name='视屏链接')
    describe = models.CharField(max_length=500, verbose_name='描述')

    class Meta:
        verbose_name = '公司视频'
        verbose_name_plural = verbose_name
        db_table = "company_video"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='产品分类')
    image = models.ImageField(upload_to='product_category/%Y/%m', verbose_name='产品分类图片')
    description = models.CharField(max_length=5000, blank=True, null=True, verbose_name='分类描述')
    content = models.TextField(blank=True, null=True, verbose_name='产品分类内容')

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = verbose_name
        db_table = "product_category"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, verbose_name='产品分类')
    name = models.CharField(max_length=255, verbose_name='产品名称')
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='产品简介')
    content = models.TextField(blank=True, null=True, verbose_name='产品详情')
    image = models.ImageField(upload_to='product/%Y/%m', verbose_name='产品图片')
    parameter = models.TextField(blank=True, null=True, verbose_name='参数')
    model = models.TextField(blank=True, null=True, verbose_name='选型')
    test = models.TextField(blank=True, null=True, verbose_name='测试')
    application = models.TextField(blank=True, null=True, verbose_name='应用')
    download = models.FileField(upload_to='product/download/%Y/%m', blank=True, null=True, verbose_name='资料下载')
    show_index = models.NullBooleanField(default=False, blank=True, null=True, verbose_name='是否展示到首页')

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = verbose_name
        db_table = "product"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='新闻标题')
    news_image = models.ImageField(upload_to='news/%Y/%m', verbose_name='新闻图片')
    content = models.TextField(blank=True, null=True, verbose_name='新闻内容')
    user = models.ForeignKey(User, verbose_name='编辑者')
    eye_count = models.IntegerField(blank=True, null=True, default=0, verbose_name='浏览量')
    thumb_count = models.IntegerField(blank=True, null=True, default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='发表时间')
    show_index = models.NullBooleanField(default=False, blank=True, null=True, verbose_name='是否展示到首页',
                                         help_text='目前首页只能显示5条')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        db_table = "news"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.title


class ApplicationCase(models.Model):
    name = models.CharField(max_length=255, verbose_name='案例名称')
    description = models.CharField(max_length=2000, blank=True, null=True, verbose_name='案例描述')
    image = models.ImageField(upload_to='application/%Y/%m', verbose_name='案例图片')
    content = models.TextField(blank=True, null=True, verbose_name='案例内容')
    show_index = models.NullBooleanField(default=False, blank=True, null=True, verbose_name='是否展示到首页',
                                         help_text='最多9条')

    class Meta:
        verbose_name = '应用案例'
        verbose_name_plural = verbose_name
        db_table = "application_case"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=255, verbose_name='职位名称')
    content = models.TextField(blank=True, null=True, verbose_name='职位内容')

    class Meta:
        verbose_name = '联系我们-招聘人才'
        verbose_name_plural = verbose_name
        db_table = "recruit"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='服务名称')
    image = models.ImageField(upload_to='service/%Y/%m', verbose_name='服务图片')
    description = models.CharField(max_length=2000, blank=True, null=True)
    content = models.TextField(blank=True, null=True, verbose_name='详细内容')

    class Meta:
        verbose_name = '服务项目'
        verbose_name_plural = verbose_name
        db_table = "service"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.name


class SiteMessage(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    phone_num = models.CharField(max_length=255, blank=True, null=True, verbose_name='电话号码')
    content = models.TextField(blank=True, null=True, verbose_name='留言内容')

    class Meta:
        verbose_name = '网站留言'
        verbose_name_plural = verbose_name
        db_table = "site_message"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.user_name


class ContactList(models.Model):
    area = models.CharField(max_length=255, verbose_name='公司大区')
    phone = models.CharField(max_length=100, verbose_name='电话')
    email = models.EmailField(verbose_name='邮箱')
    facsimile = models.CharField(max_length=255, verbose_name='传真')
    address = models.CharField(max_length=500, verbose_name='地址')

    class Meta:
        verbose_name = '联系方式'
        verbose_name_plural = verbose_name
        db_table = "contact_list"
        ordering = ['id']
        default_permissions = ("read", "change", "add", "delete")

    def __unicode__(self):
        return self.area
