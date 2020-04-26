"""Xadministration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

# 导入视图
from django.views.generic import TemplateView
from apps.users.views import LoginView, LogoutView, RegisterView

from apps.users import views as user_views

import xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # 首页、登陆、注册
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # 利用CBV编程：class base view
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    # 加入图形验证码
    url(r'^captcha/', include('captcha.urls')),

    url(r'^chat/', user_views.chat, name='chat'),
]