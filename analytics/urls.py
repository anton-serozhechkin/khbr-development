from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='analytics'),
    re_path('(?P<id>\d+)', views.article_detail, name='article_detail')
]