# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from .models import *
from django.views.generic import View, TemplateView, ListView

# Create your views here.

class Hello(TemplateView):
    template_name = 'hello.html'
    def get_context_data(self, **kwargs):
        # context = super(Hello, self).get_context_data(**kwargs)
        # context['username'] = 'hanhan'
        # context['lans'] = ['a', 'b', 'c']
        # print(context)
        # return context
        return kwargs


def users(request, pk):
    return HttpResponse(pk)


def add(req, a, b):
    c = int(a) + int(b)
    return HttpResponse(c)


class User1(View):
    def get(self, request, **kwargs):
        pk1 = kwargs.get('pk1')
        pk2 = kwargs.get('pk2')
        print(request.META)
        print(request.user)
        return HttpResponse(int(pk1) + int(pk2))


def argstest(req):
    name = req.GET.get('name')
    id = req.GET.get('id')
    ret = {'name': name, 'id': id}
    return JsonResponse(ret)


def hello(req):
    context = [1, 2, 3, 5, 6]
    return render(req, 'hello.html', {'name': context})


def index(req):
    return render(req, 'index.html')

 
def bookquery(request):
    # data = [i for i in Book.objects.all().values('name', 'price')]
    data = [model_to_dict(i, exclude=['pub_date', 'id']) for i in Book.objects.all()]
    data = [i.todict for i in Book.objects.all()]
    return JsonResponse({'status': 0, 'data': data})

def authorquery(request):
    # data = [i for i in author.objects.all().values('name', 'price')]
    # data = [model_to_dict(i, exclude=['pub_date', 'id']) for i in author.objects.all()]
    # data = [i.todict for i in Author.objects.all()]
    # 粉丝量或收入在前两位的作者
    qs = Author.objects.all()
    qsfans = qs.order_by('-fans')[:2]
    qsincome = qs.order_by('-income')[:2]
    qsret = list(set(qsfans).union(set(qsincome)))
    data = [i.todict for i in qsret]
    return JsonResponse({'status': 0, 'data': data})

class User(View):
    def get(self, request):
        return HttpResponse('hello world!')

class AuthorList(ListView):
        model = Author
        template_name = 'app1/authors.html'
        context_object_name = 'authors'
        paginate_by = 10
        def get_context_data(self, **kwargs):
            context = super(Hello, self).get_context_data(**kwargs)

# todo
