from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'index', index),
    url(r'users/(\d+)', users),
    url(r'add/(\d+)/(\d+)', add),
    url(r'users1/(?P<pk1>(\d+))/(?P<pk2>(\d+))', User1.as_view()),
    url(r'argstest', argstest),
    # url(r'hello', hello),
    url(r'bookquery/$', bookquery),
    url(r'authorquery/$', authorquery),
    url(r'users', User.as_view()),
    url(r'hello/(?P<pm>\d+)', Hello.as_view()),
]
