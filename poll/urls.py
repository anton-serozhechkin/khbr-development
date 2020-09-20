from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='poll'),
    re_path('(?P<slug>[\w-]+)', poll_detail, name='poll_detail'),
]