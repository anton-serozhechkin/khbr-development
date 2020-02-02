from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main, name='videooverview'),
    re_path('(?P<slug>[\w-]+)', video_detail, name='video-detail'),
]