from django.shortcuts import render, redirect
from django.http import Http404
from .bloggers_data import BloggerData

data = BloggerData()

def home(request):
    news = data.get_news()
    return render(request, 'bloggers/home.html', {'news': news})

def bloggers_list(request):
    bloggers = data.get_all_bloggers()
    return render(request, 'bloggers/bloggers_list.html', {'bloggers': bloggers})

def blogger_detail(request, blogger_id):
    blogger = data.get_blogger_by_id(int(blogger_id))
    if not blogger:
        raise Http404("Блогер не знайдений")
    return render(request, 'bloggers/blogger_detail.html', {'blogger': blogger})

def news_redirect(request):
    return redirect('/')
