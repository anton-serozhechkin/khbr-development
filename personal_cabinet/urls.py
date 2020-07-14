from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.personal_cabinet, {'news': True}, name='personal_cabinet'),
    re_path('&private_data/$', views.personal_cabinet, {'private_data': True}, name='private_data'),
    re_path('&change_password/$', views.personal_cabinet, {'change_password': True}, name='change_password'),
    re_path('&subscribe/$', views.personal_cabinet, {'subscribe': True}, name='subscribe'),
    re_path('&unsubscribe/$', views.personal_cabinet, {'unsubscribe': True}, name='unsubscribe'),
    re_path('&links/$', views.personal_cabinet, {'links': True}, name='links'),
]