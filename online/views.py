# coding=utf-8

from django.shortcuts import render,redirect
from online.models import User
from django.utils import timezone
from blogs.views import my_pagination
from blogs.models import BlogsManage


def login(request):
    return render(request, 'online/login.html')


def log_success(request):
    if request.method == "POST":
        # 获取表单信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print username, password
        # 对比
        userinfo = User.objects.filter(username=username, password=password)
        # 判断用户是否存在
        if bool(userinfo):
            # 查看用户是否有文章
            all_objects = BlogsManage.objects.filter(author=username)
            objects, page_range = my_pagination(request, all_objects)
            return redirect('/blogs/%s' % username, {'userinfo': userinfo, 'objects': objects, 'page_range': page_range})

        else:
            return redirect('/online/')


def account(request):
    return render(request, 'online/account.html')


def acc_success(request):
    if request.method == "POST":
        # 获取表单信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        account_time = timezone.now()
        # 将表单写入数据库
        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.account_time = account_time
        user.save()
        # 返回注册成功页面
        return render(request, 'online/acc_success.html', {'username': username})