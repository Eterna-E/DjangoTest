"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from mysite.views import here, add, math,register # <-引進add
from restaurants.views import menu
from django.views.generic.base import TemplateView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('here123/', here),
    re_path(r'(\d{1,2})/plus/(\d{1,2})', add), # <- 加入這行
    re_path(r'(\d{1,2})/math/(\d{1,2})', math),
    path('menu/',menu),
    path('vendor/', include('vendor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html')),
    path('register/', register, name='register'),
]
