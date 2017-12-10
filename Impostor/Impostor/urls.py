"""Impostor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from Login import views

# 对应域名和具体的html
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Login/', views.Login),
    url(r'^submit/', views.submit),
    url(r'^sign_up/', views.sign_up),
    url(r'^reset/', views.reset),
    url(r'^new_password/', views.new_passwords)
]
