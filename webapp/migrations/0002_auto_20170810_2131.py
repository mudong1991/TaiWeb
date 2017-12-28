# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemessage',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='\u7559\u8a00\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='sitemessage',
            name='interest_product',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u611f\u5174\u8da3\u4ea7\u54c1'),
        ),
        migrations.AlterField(
            model_name='sitemessage',
            name='phone_num',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801'),
        ),
    ]