# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse 
from django.contrib.auth.decorators import login_required
from django.views import View # 类视图的基类

# notes: login_required 的作用是要求用户登录，即登录此页面时会跳转到 settings.py 文件里设置的 LOGIN_URL
# 注释此行则会直接访问页面，不会跳转到登录页
@login_required
def firstpage(request):
    return HttpResponse('hello')

def user_list_view(req):
    user_queryset = User.objects.all()
    for user in user_queryset:
        print(user.username, user.email)
    return HttpResponse("")

class MyLogin(View):
    def get(self, request):
        nexturl = request.GET.get('next')
        return render(request, 'pages/examples/login.html', { "nexturl": nexturl})

    def post(self, request):
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username = username, password = password) # 鉴权
        print("user: %s" % user)
        ret = {}
        if user is not None:
            login(request, user) # 登录
            ret['status'] = 0
        else:
            ret['status'] = 1
        return JsonResponse(ret)

def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/login')


