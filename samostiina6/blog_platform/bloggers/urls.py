from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bloggers/', views.bloggers_list, name='bloggers_list'),
    re_path(r'^blogger/(?P<blogger_id>\d+)/$', views.blogger_detail, name='blogger_detail'),
    path('news/', views.news_redirect, name='news_redirect'),
]
