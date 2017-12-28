# -*- coding: UTF-8 -*-
# __author__ = 'MD'

from xadmin.layout import Fieldset, Main, Side, Row, FormHelper
from django.utils.translation import ugettext_lazy as _, ungettext


class ArticleAdmin(object):
    """
    文章模型数据管理注册
    """

    model_icon = 'fa fa-book'  #: 模型菜单图标
    list_display = ('title', 'user', 'portal', 'category', 'tag', 'get_comment',
                    'date_publish')  #: 列表栏目

    list_filter = ('title', 'user', 'url', 'click_count', 'like_count', 'is_recommed',
                   'date_publish', 'category', 'tag')  #: 过滤字段

    search_fields = ('name', 'author', 'publish_house')

    list_editable = ['title']

    def get_comment(self, article):
        comment = article.comment.count()
        return comment

    get_comment.short_description = "评论数"
    get_comment.is_column = True
    get_comment.allow_tags = True
    get_comment.admin_order_field = 'comment'

    form_layout = (
        Main(
            Fieldset("基本信息",
                     'title',
                     'user',
                     'content',
                     'portal',
                     'url',
                     'date_publish',
                     'category',
                     'tag'
                     ),
            Fieldset("文章属性",
                     'click_count',
                     'like_count'
                     ),
            Fieldset("其他信息",
                     'desc'
                     ),
        ),
        Side(
            Fieldset("特别信息",
                     'is_recommed'
                     )
        )
    )

    # 引入媒体文件，创建富文本
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )