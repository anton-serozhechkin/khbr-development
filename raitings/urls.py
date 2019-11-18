from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main),
    path('<int:id>', raiting_detail, name='raiting_detail'),
]