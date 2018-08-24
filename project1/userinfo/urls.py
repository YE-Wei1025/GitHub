from django.conf.urls import *
from .views import *

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^loginout/$', login_out, name='login_out'),
    url(r'^info/$', user_info, name='user_info'),
    url(r'^useraddress/$', user_address, name='useraddress'),
    url(r'^addads/$', add_ads, name='addads'),
    url(r'^editads/$', edit_ads, name='editads'),
    url(r'^deleteads/$', delete_ads, name='deleteads'),
]