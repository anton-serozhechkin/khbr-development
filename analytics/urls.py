from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main),
    re_path('(?P<category>\d+)', views.show_categ),
    #re_path('(?P<category>&<id>\d+)', views.show_article)
]