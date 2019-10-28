from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main),
    re_path('(?P<id>\d+)', event_detail),
]