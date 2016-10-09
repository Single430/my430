# coding=utf-8
from django.contrib import admin
from blogs.models import BlogsManage
# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('Type', {'fields': ['blog_type']}),
        ('Images', {'fields': ['blog_imgurl']}),
        ('Body', {'fields': ['body']}),
        ('Article_description', {'fields': ['body_des']}),
        ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'author', 'publish_date', 'body_des')
    list_filter = ['publish_date']  # 侧边栏
    search_fields = ['title']   # 搜索功能


admin.site.register(BlogsManage, BlogsAdmin)