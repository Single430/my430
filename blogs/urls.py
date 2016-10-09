"""blogManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))new_sub_article
"""
from django.conf.urls import url, include
from django.contrib import admin
from blogs import views
from online.views import login

urlpatterns = [
        url(r'^$', login, name='login'),
        url(r'^(?P<username>[\w]+)/$', views.index, name='index'),
        url(r'^article/(?P<username>[\w]+)/(?P<blog_body_id>[0-9]+)', views.article, name='article'),

        url(r'^article/(?P<username>[\w]+)/Python/', views.python, name='python'),
        url(r'^article/(?P<username>[\w]+)/Linux/', views.linux, name='linux'),

        url(r'^add_article/(?P<username>[\w]+)', views.add_article, name='add_article'),
        url(r'^sub_article/(?P<username>[\w]+)', views.sub_article, name='sub_article'),

        url(r'^del_article/(?P<username>[\w]+)=(?P<blog_body_id>[0-9]+)', views.del_article, name='del_article'),
        url(r'^edit_article/(?P<username>[\w]+)=(?P<blog_body_id>[0-9]+)', views.edit_article, name='edit_article'),

        url(r'^new_sub_article/(?P<blog_body_id>[0-9]+)', views.new_sub_article, name='new_sub_article'),
        # url(r'^list/', views.listing, name='listing'),
]