import random
from msilib.schema import ListView

from django_filters.views import BaseFilterView
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from  .forms import *

from .models import User,UserExtension,Dog,Cat
# Create your views here.
from .filters import CatFilter, DogFilter


def homepage(request):
    context = {

    }

    return render(request, 'pathtml/index.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        message=''
        if request.method=='POST':
            name_get=request.POST.get('username')
            pwd_get=request.POST.get('password')

            user=authenticate(request,username=name_get,password=pwd_get)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                else:
                    message='此账号被冻结！'
            else:
                message='用户名或密码错误!'

    context={
        'message':message,
    }

    return render(request,'pathtml/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('login')

def findpsView(request):
    tips=""

    button = '获取验证码'	# 模板上下文：按钮提示内容
    VCodeInfo = False 	# 模板上下文：是否已发送验证码
    password = False	# 模板上下文：是否生成密码输入框
    zh=True
    if request.method == 'POST':

        u = request.POST.get('username')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        VCode = request.POST.get('VCode', '') # 模板上下文：产生的验证码
        user = User.objects.filter(username=u)
        # 用户不存在
        if not user:
            tips = '用户' + u + '不存在'
        else:
            # 判断验证码是否已发送
            if not request.session.get('VCode', ''):
                # 发送验证码并将验证码写入session
                button = '重置密码'
                tips = '验证码已发送'
                zh=False
                password = True
                VCodeInfo = True
                VCode = str(random.randint(000000, 999999))
                request.session['VCode'] = VCode
                user[0].email_user('找回密码', VCode)
            # 匹配输入的验证码是否正确
            elif VCode == request.session.get('VCode'):
                if p1!=p2:
                    tips="两次输入的密码不一致！"
                    VCodeInfo = False
                    password = False
                    del request.session['VCode']
                else:
                # 密码加密处理并保存到数据库
                    dj_ps = make_password(p1, None, 'pbkdf2_sha256')
                    user[0].password = dj_ps
                    user[0].save()
                    del request.session['VCode']
                    return redirect('login')
            # 输入验证码错误
            else:
                tips = '验证码错误，请重新获取'
                VCodeInfo = False
                password = False
                del request.session['VCode']

    context={
        'tips':tips,
        'VCodeInfo': VCodeInfo,
        'password':password,
        'button':button,
        'zh':zh
    }

    return render(request, 'pathtml/findpwd.html', context  )

def register(request):

    message = ""
    if request.method == 'POST':

            name_get = request.POST.get('username'),
            pwd1_get = request.POST.get('password1'),
            pwd2_get = request.POST.get('password2'),
            email_get = request.POST.get('email'),
            phone_get = request.POST.get('phone')
            # try:
            if pwd1_get[0] == pwd2_get[0]:
                new_user = User.objects.create_user(username=name_get[0], password=pwd1_get[0],
                                                            email=email_get[0])
                new_user.save()
                UserExtension.objects.create(user=new_user, phone=phone_get).save()
                return redirect('login')
            else:
                message = '两次输入的密码不一致！'
            # except:
            #         message = "用户名已经被注册!"


    context = {

        'message': message
    }
    return render(request, 'pathtml/register.html', context)
@login_required(login_url='login')
def modify_pwd(request):
    message=''
    if request.method=='POST':
        old_pwd=request.POST.get('old_pwd')
        new_pwd=request.POST.get('new_pwd')
        repeat_pwd=request.POST.get('repeat_pwd')

        user=authenticate(request,username=request.user.username,password=old_pwd)
        if user is not None :
            if User.is_active:
                if new_pwd !=repeat_pwd:
                    message='两次输入的密码不一致'
                else:
                    user.set_password(new_pwd)
                    user.save()
                    logout(request)
                    return redirect('login')
            else:
                message='此账号已被冻结！'
        else:
            message='原密码输入错误！'

    context={
        'message':message
    }
    return render(request,'pathtml/change-password.html',context)


def dog(request):
    dog = Dog.objects.all()
    myFilter = DogFilter(request.GET, queryset=dog)
    dog = myFilter.qs
    paginator = Paginator(dog, 12)
    total_dog = dog.count()

    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'dog': dog,
        'total_dog': total_dog,
        'myFilter': myFilter,
        'page_obj': page_obj,
        'paginator': paginator,
        'is_paginated': True,
    }

    return render(request, 'pathtml/dog.html', context=context)

def cat(request):

    cat=Cat.objects.all()
    myFilter=CatFilter(request.GET,queryset=cat)
    cat=myFilter.qs
    paginator = Paginator(cat, 12)
    total_cat = cat.count()

    page=request.GET.get('page')
    page_obj=paginator.get_page(page)


    context={
        'cat':cat,
        'total_cat': total_cat,
        'myFilter':myFilter,
        'page_obj':page_obj,
        'paginator':paginator,
        'is_paginated': True,
    }

    return render(request,'pathtml/cat.html',context=context)

def dog_detail(request,pk):
    dog_detail=Dog.objects.get(id=pk)

    context={
    'dog_detail':dog_detail
    }

    return render(request,'pathtml/detail-info.html',context=context)

def cat_detail(request,pk):
    cat_detail=Cat.objects.get(id=pk)

    context = {
        'cat_detail': cat_detail
    }

    return render(request,'pathtml/detail-info.html',context=context)


@login_required(login_url='login')
def userinfo(request,id):

    user=User.objects.get(id=id)
    profile=UserExtension.objects.get(user_id=id)

    context={
            'profile':profile,
            'user':user,

    }

    return render(request,'pathtml/xs.html',context=context)
@login_required(login_url='login')
def xgtx(request,id):
    user = User.objects.get(id=id)
    profile = UserExtension.objects.get(user_id=id)
    if request.method=='POST':
        if request.user!=user:
            return HttpResponse("你没有权限修改该用户信息！")

        profile_form=userForm(request.POST,request.FILES)
        if profile_form.is_valid():
            profile_cd=profile_form.cleaned_data
            profile.birthday = profile_cd['birthday']
            profile.phone=profile_cd['phone']
            profile.gender = profile_cd['gender']
            profile.address = profile_cd['address']
            profile.like = profile_cd['like']
            profile.aboutme = profile_cd['aboutme']
            if 'image' in request.FILES:
                profile.image=profile_cd['image']
            profile.save()
            return redirect('userinfo',id=id)
        else:
            return HttpResponse("输入有误")
    elif request.method=='GET':
        profile_form=userForm()
        context = {
        'profile_form':profile_form,
        'profile': profile,
        'user': user,

        }
        return render(request, 'pathtml/tx.html', context=context)




