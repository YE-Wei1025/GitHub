from django.contrib import messages
from django.contrib.auth.hashers import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import *
from memberapp.models import Goods
from .models import *
from django.db import *
import logging

# Create your views here.


# 注册处理
def register(request):
    # 判断请求方式
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        # 声明一个新用户
        new_user = UserInfo()
        new_user.name = request.POST.get('user_name')
        # 查询并判断用户是否存在
        try:
            a = UserInfo.objects.filter(name=new_user.name)
            if a:
                return render(request, 'register.html', {'message': '该用户名已存在'})
            # 判断密码是否一致
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request, 'register.html', {'message': '两次密码输入不一致'})
            # 对密码进行加密，并保存新用户信息
        new_user.password = make_password(request.POST.get('pwd'), 'abc', 'pbkdf2_sha256')
        new_user.email = request.POST.get('email')
        new_user.phone = request.POST.get('phone')
        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
        # 注册成功返回登录页面
        return render(request, 'login.html')
    return redirect('/user/register/')


# 登录处理
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = UserInfo()
        user.name = request.POST.get('name')
        user.password = request.POST.get('password')
        try:
            find_user = UserInfo.objects.filter(name=user.name)
            if len(find_user) <= 0:
                messages.add_message(request, messages.ERROR, '该用户未注册')
                return redirect('/user/login/')
            if not check_password(user.password, find_user[0].password):
                return render(request, 'login.html', {'user_info': user, 'message_error': '密码输入不正确'})
            request.session['user_id'] = find_user[0].id
            request.session['user_name'] = user.name
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.COOKIES.get('url'):
            url = request.COOKIES.get('url')
            res = redirect(url)
            res.delete_cookie('url')
            return res
        return redirect('/')
    return redirect('/user/login/')


# 退出处理
def login_out(request):
    try:
        if request.session['user_name']:
            del request.session['user_id']
            del request.session['user_name']
    except DatabaseError as e:
        logging.warning(e)
    return redirect('/user/login')


# 显示用户信息
def user_info(request):
    try:
        rec_view_list = list()
        userinfo = get_object_or_404(UserInfo, name=request.session.get('user_name'))
        user_id = request.session.get('user_id')
        adss = Address()
        adss = Address.objects.filter(user_id=user_id)
        if request.COOKIES.get('Recently_Viewed', None):
            rec_view = request.COOKIES.get('Recently_Viewed', None)
            list_view = rec_view.split(',')
            for i in list_view:
                rec_view_list.append(Goods.objects.get(id=i))
        else:
            rec_view_list = []
    except ObjectDoesNotExist as e:
        logging.warning(e)
    if len(adss) > 0:
        content = {'userinfo': userinfo, 'rec_view': rec_view_list, 'adss': adss[0]}
    else:
        content = {'userinfo': userinfo, 'rec_view': rec_view_list, 'adss': ''}
    return render(request, 'user_center_info.html', content)


# 显示用户的地址
def user_address(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    return render(request, 'user_center_site.html', {'adss': adss})


# 添加一个新地址
def add_ads(request):
    user_id = request.session.get('user_id')
    addressee = request.POST.get('addressee')
    Detailed_address = request.POST.get('Detailed_address')
    phone = request.POST.get('phone')
    try:
        userd_ = UserInfo.objects.get(id=user_id)
        Address.objects.create(name=addressee, ads=Detailed_address, phone=phone, user=userd_)
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return redirect('useraddress')


# 添加一个新地址
def edit_ads(request):
    user_id = request.session.get('user_id')
    ida = request.POST.get('ida')
    addressee = request.POST.get('addresseed')
    Detailed_address = request.POST.get('Detailed_addressd')
    phone = request.POST.get('phone')
    try:
        userd_ = UserInfo.objects.get(id=user_id)
        Address.objects.filter(id=ida).update(name=addressee, ads=Detailed_address, phone=phone, user=userd_)
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return redirect('useraddress')


# 删除id=adid的地址
def delete_ads(request):
    user_id = request.session.get('user_id')
    adid = request.GET.get('adid')
    try:
        delads = Address.objects.get(user_id=user_id, id=adid)
        delads.delete()
    except BaseException as e:
        logging.warning(e)
    return redirect('useraddress')
