from django.urls import path
from . import views

urlpatterns = [
    path("install/", views.install_demo, name="install_demo"),
    path("duikt_page_osypov/", views.show_page, name="duikt_page_osypov"),
]
