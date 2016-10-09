"""Portal_site URL Configuration

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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from online import views
from blogs.views import index

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^account/$', views.account, name='account'),
    url(r'^acc_success/$', views.acc_success, name='acc_success'),
    url(r'^log_success/$', views.log_success, name='log_success'),
]
