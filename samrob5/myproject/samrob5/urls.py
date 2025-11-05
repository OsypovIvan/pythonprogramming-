from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_info, name='my_info'),
]
