from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main),
    re_path('(?P<slug>\d+)', views.article_by_categ),
    re_path('(?P<slug>\<id>\d+)', views.article)
]