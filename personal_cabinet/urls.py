from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.personal_cabinet, name='personal_cabinet'),
    re_path('private_data', views.personal_cabinet, name='private_data'),
    re_path('change_password', views.personal_cabinet, name='change_password'),
    re_path('subscribe', views.personal_cabinet, name='subscribe'),
    re_path('unsubscribe', views.personal_cabinet, name='unsubscribe'),
    re_path('links', views.personal_cabinet, name='links'),
    re_path('delete_account', views.personal_cabinet, name='delete_account'),
]