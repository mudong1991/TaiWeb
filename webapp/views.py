# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
import json
import os
from django.conf import settings
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import (HttpResponse, HttpResponseForbidden, HttpResponseNotFound, Http404, StreamingHttpResponse)
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from webapp import models
from django.urls import reverse
from webapp.forms import *
from webapp.util import *

# 定义一个日志器
logger = logging.getLogger('webapp.views')


# 定义全局变量函数字典，并设置到settings中
def global_setting(request):
    SITE_NAME = settings.SITE_NAME
    SITE_KEYWORDS = settings.SITE_KEYWORDS
    SITE_DESC = settings.SITE_DESC
    SITE_AUTHOR = settings.SITE_AUTHOR
    CHAT_QQ = settings.CHAT_QQ

    # 首页欢迎信息title
    title_index = settings.SITE_INDEX_TITLE
    # 广告
    ad_list = models.Ad.objects.all()
    # 产品分类
    product_category_list = models.ProductCategory.objects.all()
    # 应用案例
    application_list = models.ApplicationCase.objects.filter(show_index=True)
    # 服务
    service_list = models.Service.objects.all()

    return locals()


# 分页代码
def getPage(request, query_list):
    paginator = Paginator(query_list, 5)
    try:
        page = int(request.GET.get('page', 1))
        query_pag_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        query_pag_list = paginator.page(1)  # 如果用户输入错误的page数返回第一个页
    return query_pag_list


# Create your views here.
# 首页
def index(request):
    # 网站标题
    site_menu = '首页'
    active_menu = 'index'
    # 关于泰雷兹
    company_profile = models.CompanyIntro.objects.first()
    # 公司视频
    company_video_list = models.CompanyVideo.objects.all()[:2]
    # 产品分类
    product_category_list = models.ProductCategory.objects.all()
    # 新闻
    news_list = models.News.objects.filter(show_index=True)[:5]
    # 应用案例
    application_list = models.ApplicationCase.objects.filter(show_index=True)[:9]
    return render(request, get_template('index.html'), locals())


# 服务项目
def service(request):
    service_id = request.GET.get('id', '')
    if service_id:
        try:
            service_obj = models.Service.objects.get(id=service_id)
        except:
            raise Exception('找不到相关服务项目！')
        # 网站标题
        site_menu = service_obj.name
        active_menu = 'service'
        active_child_menu = int(service_obj.id)
        # 内容导航
        content_nav_list = [{'name': '服务项目', 'url': reverse('service')}]

        return render(request, get_template('service-detail'), locals())
    else:
        # 网站标题
        site_menu = '服务项目'
        active_menu = 'service'
        active_child_menu = ''

        service_list = models.Service.objects.all()
        return render(request, get_template('service'), locals())


# 应用案例
def application(request):
    application_id = request.GET.get('id', '')
    if application_id:
        try:
            application_obj = models.ApplicationCase.objects.get(id=application_id)
        except:
            raise Exception('找不到相关应用案例！')
        # 网站标题
        site_menu = application_obj.name
        active_menu = 'application'
        active_child_menu = int(application_obj.id)
        # 内容导航
        content_nav_list = [{'name': '应用案例', 'url': reverse('application')}]

        return render(request, get_template('application-detail'), locals())
    else:
        # 网站标题
        site_menu = '服务项目'
        active_menu = 'application'
        active_child_menu = ''

        application_list = models.ApplicationCase.objects.all()
        return render(request, get_template('application'), locals())


# 产品类
def product_category(request):
    product_category_id = request.GET.get('id', '')
    if product_category_id:
        try:
            product_category_obj = models.ProductCategory.objects.get(id=product_category_id)
        except:
            raise Exception('找不到相关产品类！')
        # 产品列表
        product_list = models.Product.objects.filter(product_category=product_category_obj)

        # 网站标题
        site_menu = product_category_obj.name
        active_menu = 'product_category'
        active_child_menu = int(product_category_id)
        # 内容导航
        content_nav_list = [{'name': '产品中心', 'url': reverse('product_category')}]

        return render(request, get_template('product_category_detail'), locals())
    else:
        # 网站标题
        site_menu = '产品中心'
        active_menu = 'product_category'
        active_child_menu = ''

        product_category_list = models.ProductCategory.objects.all()

        # 分页
        # product_category_list = getPage(request, product_category_list)
        # page_num_range = range(1, product_category_list.paginator.num_pages+1)

        return render(request, get_template('product_category'), locals())


def product(request):
    product_id = request.GET.get('id', '')
    if product_id:
        try:
            product_obj = models.Product.objects.get(id=product_id)
        except:
            raise Exception('没有找到相关产品信息！')

        product_category_obj = product_obj.product_category

        # 网站标题
        site_menu = product_obj.name
        active_menu = 'product_category'
        active_child_menu = int(product_category_obj.id)
        # 内容导航
        content_nav_list = [{'name': '产品中心', 'url': reverse('product_category')},
                            {'name': product_category_obj.name, 'url': reverse('product_category')
                                                                       + '?id=' + str(product_category_obj.id)}
                            ]

        return render(request, get_template('product'), locals())
    else:
        raise Exception('没有找到相关产品信息！')


# 关于我们
def about_us(request):
    # 网站标题
    site_menu = '关于我们'
    active_menu = 'about_us'

    return render(request, get_template('about_us.html'), locals())


# 公司介绍
def company_intro(request):
    # 网站标题
    site_menu = '公司介绍'
    active_menu = 'about_us'
    active_child_menu = 'company_intro'
    # 内容导航
    content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}]

    company_intro_obj = models.CompanyIntro.objects.first()

    return render(request, get_template('company_intro.html'), locals())


# 发展历程
def develop_history(request):
    # 网站标题
    site_menu = '发展历程'
    active_menu = 'about_us'
    active_child_menu = 'develop_history'
    # 内容导航
    content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}]

    develop_history_list = models.DevelopHistory.objects.all()

    return render(request, get_template('develop_history'), locals())


# 公司文化
def culture(request):
    # 网站标题
    site_menu = '公司文化'
    active_menu = 'about_us'
    active_child_menu = 'culture'
    # 内容导航
    content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}]

    culture_obj = models.CompanyCulture.objects.first()

    return render(request, get_template('culture'), locals())


# 组织架构
def structure(request):
    # 网站标题
    site_menu = '组织架构'
    active_menu = 'about_us'
    active_child_menu = 'structure'
    # 内容导航
    content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}]

    structure_obj = models.CompanyStructure.objects.first()

    return render(request, get_template('structure'), locals())


# 组织架构
def news(request):
    news_id = request.GET.get('id', '')
    if news_id:
        try:
            news_obj = models.News.objects.get(id=news_id)
        except:
            raise Exception('没有找到相关新闻！')
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        if not request.session.has_key('eye_count{0}{1}'.format(news_id, str(ip))):
            news_obj.eye_count += 1
            news_obj.save()
            request.session['eye_count{0}{1}'.format(news_id, str(ip))] = True
        # 网站标题
        site_menu = news_obj.title
        active_menu = 'about_us'
        active_child_menu = 'news'
        # 内容导航
        content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}, {'name': '新闻中心', 'url': reverse('news')}]

        return render(request, get_template('news-detail'), locals())
    else:
        # 网站标题
        site_menu = '新闻中心'
        active_menu = 'about_us'
        active_child_menu = 'news'
        # 内容导航
        content_nav_list = [{'name': '关于我们', 'url': reverse('about_us')}]

        news_list = models.News.objects.all()
        # 分页
        news_list = getPage(request, news_list)
        page_num_range = range(1, news_list.paginator.num_pages+1)
        return render(request, get_template('news'), locals())


# 新闻点赞
@csrf_exempt
def news_thumbs(request):
    if request.method == 'POST':
        news_id = request.POST.get('news_id', '')
        try:
            news_obj = models.News.objects.get(id=news_id)
        except:
            raise Exception('没有找到相关新闻！')

        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        if not request.session.has_key('thumb_count{0}{1}'.format(news_id, ip)):
            news_obj.thumb_count += 1
            news_obj.save()
            request.session['thumb_count{0}{1}'.format(news_id, ip)] = True

            json_return = json.dumps({'result': '1', 'message': news_obj.thumb_count}, indent=4)
            return HttpResponse(json_return, content_type='application/json', status=200)
        else:
            json_return = json.dumps({'result': '0', 'message': '今天你已经对该文章点过赞了'}, indent=4)
            return HttpResponse(json_return, content_type='application/json', status=200)


# 联系我们
def contact_us(request):
    # 网站标题
    site_menu = '联系我们'
    active_menu = 'contact_us'

    return render(request, get_template('contact_us.html'), locals())


# 联系方式
def contact_kinds(request):
    # 网站标题
    site_menu = '联系方式'
    active_menu = 'contact_us'
    active_child_menu = 'contact_kinds'
    # 内容导航
    content_nav_list = [{'name': '联系我们', 'url': reverse('contact_us')}]
    # 联系方式列表
    contact_list = models.ContactList.objects.all()
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            models.SiteMessage.objects.create(user_name=message_form.cleaned_data['username'],
                                                             email=message_form.cleaned_data['email'],
                                                             phone_num=message_form.cleaned_data['phone_num'],
                                                             content=message_form.cleaned_data['content'])
            success_message = '提交成功，请耐心等待我们的联系！'
            message_form = MessageForm()
            return render(request, get_template('contact_kinds.html'), locals())
        else:
            error_message = "表单填写不规范！"
            message_form = MessageForm()
            return render(request, get_template('contact_kinds.html'), locals())
    else:
        message_form = MessageForm()
        return render(request, get_template('contact_kinds.html'), locals())


# 招聘
def recruit(request):
    # 网站标题
    site_menu = '诚聘英才'
    active_menu = 'contact_us'
    active_child_menu = 'recruit'

    # 内容导航
    content_nav_list = [{'name': '联系我们', 'url': reverse('contact_us')}]

    return render(request, get_template('recruit.html'), locals())


# 搜索
def search(request):
    keywords = request.GET.get('search', '')
    # 网站标题
    site_menu = '搜索结果'
    result_list = []

    if keywords:
        # 服务
        service_obj_list = models.Service.objects.filter(name__contains=keywords)
        for service_obj in service_obj_list:
            result_list.append({'title': service_obj.name, 'url': reverse('service') + "?id=" + str(service_obj.id)})
        # 产品分类
        product_category_list = models.ProductCategory.objects.filter(name__contains=keywords)
        for product_category_obj in product_category_list:
            result_list.append({'title': product_category_obj.name, 'url': reverse('product_category') + "?id=" + str(product_category_obj.id)})
        # 产品
        product_list = models.Product.objects.filter(name__contains=keywords)
        for product_obj in product_list:
            result_list.append({'title': product_obj.name, 'url': reverse('product') + "?id=" + str(product_obj.id)})
        # 案例
        app_list = models.ApplicationCase.objects.filter(name__contains=keywords)
        for app_obj in app_list:
            result_list.append({'title': app_obj.name, 'url': reverse('application') + "?id=" + str(app_obj.id)})

    return render(request, get_template('search.html'), locals())