from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .bloggers_data import BloggerData

data = BloggerData()

def home(request):
    news = data.get_news()
    html = "<h1>Головна сторінка</h1>"
    html += "<h2>Актуальні новини</h2><ul>"
    for n in news:
        html += f"<li>{n}</li>"
    html += "</ul>"
    html += '<a href="/bloggers/">Переглянути блогерів</a>'
    return HttpResponse(html)

def bloggers_list(request):
    bloggers = data.get_all_bloggers()
    html = "<h1>Список блогерів</h1><table border='1'><tr><th>Ім'я</th><th>Категорія</th><th>Опис</th></tr>"
    for id, b in bloggers.items():
        html += f"<tr><td><a href='/blogger/{id}/'>{b['name']}</a></td><td>{b['category']}</td><td>{b['description']}</td></tr>"
    html += "</table>"
    html += '<br><a href="/">На головну</a>'
    return HttpResponse(html)

def blogger_detail(request, blogger_id):
    blogger = data.get_blogger_by_id(int(blogger_id))
    if not blogger:
        raise Http404("Блогер не знайдений")
    html = f"<h1>{blogger['name']}</h1>"
    html += f"<p>Категорія: {blogger['category']}</p>"
    html += f"<p>{blogger['description']}</p>"
    html += "<h3>Соцмережі</h3><ul>"
    for platform, link in blogger['social'].items():
        html += f"<li><a href='{link}' target='_blank'>{platform}</a></li>"
    html += "</ul><h3>Останні публікації</h3><ul>"
    for post in blogger['posts']:
        html += f"<li>{post}</li>"
    html += "</ul><a href='/bloggers/'>Назад до списку блогерів</a>"
    return HttpResponse(html)

def news_redirect(request):
    return redirect('/')  # переадресація на головну
