from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='poll'),
    path('rrr/', poll_detail, name='poll_detail'),
]