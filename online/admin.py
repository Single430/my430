# coding=utf-8
from django.contrib import admin
from online.models import User


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['username']}),
        ('Password', {'fields': ['password']}),
        ('E-mail', {'fields': ['email']}),
        ('Acount date', {'fields': ['account_time'], 'classes': ['collapse']}),
    ]
    list_display = ('username', 'password', 'email', 'account_time')
    search_fields = ['username']   # 搜索功能
    list_filter = ['account_time']  # 侧边栏

admin.site.register(User, UserAdmin)