"""project1 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from memberapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('userinfo.urls')),
    url(r'^', include('memberapp.urls')),
    url(r'^cart/', include('cartinfo.urls')),
    url(r'^detail/', deatil_one),
    url(r'^prolist/$', prolist_list, name='goodslist'),
url(r'^test/$', TemplateView.as_view(template_name="test.html"), name='test'),
]
