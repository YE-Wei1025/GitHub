from django.conf.urls import *
# from cartinfo.views import *
from cartinfo.views import *

urlpatterns = [
    url(r'^$', cart_info, name='cart'),
    url(r'^orderlist/', order_list, name='orderlist'),
    url(r'^placeorder/', place_order, name='placeorder'),
    url(r'^addcart/', add_cart),
    url(r'^deletecart/', delete_cart),
    url(r'^cartcount/', cart_count),
    url(r'^addorder/', add_order),
]