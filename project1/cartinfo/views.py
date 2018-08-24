import json
import logging

import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect

from cartinfo.models import *


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goods = CartInfo.objects.filter(user=user_id)
    user_id = request.session.get('user_id')
    mycartc = 0
    if user_id:
        mycartc = CartInfo.objects.filter(user=user_id).count()
    return render(request, 'cart.html', {'find_goods': find_goods, 'mycartc': mycartc})


# 购物车数量
def cart_count(request):
    user_id = request.session.get('user_id')
    mycartc = CartInfo.objects.filter(user=user_id).count()
    cart_foods = {'mycartc': mycartc}
    return HttpResponse(json.dumps(cart_foods))


# 显示订单列表
def order_list(request):
    user_id = request.session.get('user_id')
    orders = Order.objects.filter(user=user_id)
    for order in orders:
        order.cals = json.loads(order.cals)
    return render(request, 'user_center_order.html', {'orders': orders})


# 显示订单地址
def place_order(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {'adss': adss}
    return render(request, 'place_order.html', content)


# 添加一个新的购物车，购物车细节和计数和其他东西将被保存
def add_cart(request):
    new_cart = CartInfo()
    user_id = request.session.get('user_id')
    good_id = request.GET.get('good_id')
    good_count = request.GET.get('gcount')
    good_ = Goods.objects.filter(id=good_id)
    user_ = UserInfo.objects.get(id=user_id)
    if len(good_) > 0:
        new_cart.user = user_
        new_cart.good = good_[0]
    else:
        redirect('/cart/')
    new_cart.ccount = int(good_count)
    try:
        oldgo = CartInfo.objects.filter(good_id=good_id, user_id=user_id)
        if len(oldgo) > 0:
            oldgo[0].ccount = oldgo[0].ccount + int(good_count)
            oldgo[0].save()
        else:
            new_cart.save()
    except BaseException as e:
        logging.warning(e)
        countent = {'status': 'OK', 'text': '添加数据失败'}
        return HttpResponse(json.dumps(countent))
    countent = {'status': 'OK', 'text': '添加数据成功'}
    return HttpResponse(json.dumps(countent))


# 删除购物车
def delete_cart(request):
    user_id = request.session.get('user_id')
    cart_id = request.GET.get('cart_id')
    try:
        delcart = CartInfo.objects.filter(user_id=user_id, id=cart_id)
        delcart.delete()
    except BaseException as e:
        logging.warning(e)
    content = {'status': 'OK', 'text': '删除成功'}
    return HttpResponse(json.dumps(content))


# 增加一个新的订单，广告是地址，cals是选择的货物，acot是货物的数量
def add_order(request):
    user_id = request.session.get('user_id')
    ads = request.POST.get('ads')
    cals = request.POST.get('cals')
    acot = request.POST.get('acot')
    acounts = request.POST.get('acounts')
    orderTime = datetime.datetime.now(). strftime('%Y%m%d%H%M%S')
    try:
        userd_ = UserInfo.objects.filter(id=user_id)
        Order.objects.create(user=userd_, orderNo=orderTime, ads=ads, acot=acot, acounts=acounts, cals=cals)
    except BaseException as e:
        logging.warning(e)
    content = {'status': 'OK', 'text': '删除成功'}
    return HttpResponse(json.dumps(content))