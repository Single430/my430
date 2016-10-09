# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField
# Create your models here.


class BlogsManage(models.Model):
    title = models.CharField(max_length=255)
    # body = models.TextField('内容', default='', blank=True)
    body_des = models.TextField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField('date published')
    blog_type = models.CharField(max_length=50)
    blog_imgurl = models.CharField(max_length=50, null=True)

    # 仅修改 body 字段
    body = UEditorField('内容', height=300, width=1000,
        default='', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')