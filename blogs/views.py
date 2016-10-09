# coding=utf-8
import time

from django.shortcuts import render, redirect
from blogs.models import BlogsManage
from online.models import User
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage


# Create your views here.


# 404
def page_not_found(request):
    return render(request, 'blogs/404.html')


def page_error(request):
    return render(request, 'blogs/404.html')


# 主页
def index(request, username):
    # print username
    userinfo = User.objects.filter(username=username)
    all_objects = BlogsManage.objects.filter(author=username)
    objects, page_range = my_pagination(request, all_objects)
    return render_to_response('blogs/index.html', {'userinfo': userinfo, 'objects': objects, 'page_range': page_range})


# 文章详细内容
def article(request, blog_body_id='', username=''):
    userinfo = User.objects.filter(username=username)
    # print blog_body_id, username
    try:
        blog_content = BlogsManage.objects.get(id=blog_body_id, author=username)
        return render(request, 'blogs/view.html',
                      {'userinfo': userinfo, 'blog_content': blog_content})
    except Exception, e:
        print '======%s=====' % e
        return render(request, 'blogs/404.html')


# 这里是python标签文章
def python(request, username):
    # 这里也可以使用python_blog = BlogBody.objects.filter(blog_type=’Python’)来代替执行sql语句，效果是一样的。
    # sql = 'select id, title, blog_type, publish_date, body_des from BlogsManage WHERE blog_type="python"'
    userinfo = User.objects.filter(username=username)
    python_blog = BlogsManage.objects.filter(author=username, blog_type='Python')
    return render(request, 'blogs/python_list.html',
                  {'userinfo': userinfo, 'python_blog': python_blog})


# 这里是linux标签文章
def linux(request, username):
    # 这里也可以使用python_blog = BlogBody.objects.filter(blog_type=’Python’)来代替执行sql语句，效果是一样的。
    # sql = 'select id, title, blog_type, publish_date, body_des from BlogsManage WHERE blog_type="python"'
    userinfo = User.objects.filter(username=username)
    linux_blog = BlogsManage.objects.filter(author=username, blog_type='Linux')
    return render(request, 'blogs/linux_list.html',
                  {'userinfo': userinfo, 'linux_blog': linux_blog})


# 这里是文章新建
def add_article(request, username):
    userinfo = User.objects.filter(username=username)
    return render(request, 'blogs/add_article.html', {'userinfo': userinfo})


# 文章保存到数据库
def sub_article(request, username):
    if request.method == 'POST':
        mytype = request.POST.get('article_type')
        title = request.POST.get('article_title')
        body = request.POST.get('article_body')
        body_des = request.POST.get('article_summary')
        author = request.POST.get('article_author')
        updb = BlogsManage(title=title, body=body, blog_type=mytype,
                           publish_date=time.strftime("%Y-%m-%d %X", time.localtime()),
                           author=author, blog_imgurl="/static/blogs/images/text01.jpg", body_des=body_des)
        updb.save()
        try:
            userinfo = User.objects.filter(username=username)
            python_blog = BlogsManage.objects.filter(author=username, blog_type=mytype)
            return render(request, 'blogs/python_list.html',
                          {'userinfo': userinfo, 'python_blog': python_blog})
        except:
            return render(request, 'blogs/404.html')


# 文章删除
def del_article(request, blog_body_id, username):
    BlogsManage.objects.get(id=blog_body_id, author=username).delete()
    userinfo = User.objects.filter(username=username)
    all_objects = BlogsManage.objects.filter(author=username)
    objects, page_range = my_pagination(request, all_objects)
    return render_to_response('blogs/index.html', {'userinfo': userinfo, 'objects': objects, 'page_range': page_range})


# 文章编辑
def edit_article(request, blog_body_id, username):
    userinfo = User.objects.filter(username=username)
    try:
        blogs = BlogsManage.objects.filter(id=blog_body_id, author=username)
        return render(request, 'blogs/edit_article.html',
                      {'userinfo': userinfo, 'blogs': blogs})
    except Exception, e:
        print '======%s=====' % e
        return render(request, 'blogs/404.html')


# 文章保存到数据库
def new_sub_article(request, blog_body_id):
    if request.method == 'POST':
        mytype = request.POST.get('article_type')
        title = request.POST.get('article_title')
        body = request.POST.get('article_body')
        body_des = request.POST.get('article_summary')
        author = request.POST.get('article_author')

        updb = BlogsManage(id=blog_body_id, title=title, body=body, blog_type=mytype,
                           publish_date=time.strftime("%Y-%m-%d %X", time.localtime()),
                           author=author, body_des=body_des, blog_imgurl="/static/blogs/images/text01.jpg")
        # flag_blog = BlogsManage.objects.get(id=blog_body_id)
        try:
            BlogsManage.objects.get(id=blog_body_id).delete()
            updb.save()
            return redirect('/blogs/article/%s/'%author + mytype)
        except:
            return render(request, 'blogs/index.html')


# 分页
# def listing(request):
#     all_objects = BlogsManage.objects.all()
#     objects, page_range = my_pagination(request, all_objects)
#     return render_to_response('blogs/index.html', {'objects': objects, 'page_range': page_range})


def my_pagination(request, queryset, display_amount=3):
    # 按参数分页
    paginator = Paginator(queryset, display_amount)
    try:
        # 得到request中的page参数
        page = int(request.GET.get('page'))
    except:
        # 默认为1
        page = 1
    try:
        # 尝试获得分页列表
        objects = paginator.page(page)
    # 如果页数不存在
    except EmptyPage:
        # 获得最后一页
        objects = paginator.page(paginator.num_pages)
    # 如果不是一个整数
    except:
        # 获得第一页
        objects = paginator.page(1)
    # 根据参数配置导航显示范围
    page_range = list(paginator.page_range)
    return objects, page_range


