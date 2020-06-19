from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='analytics'),
    path('analytics/', views.article_index, name='analytics_index'),
    re_path('analytics/(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)', views.article_detail, name='article_detail'),
    re_path('analytics/(?P<category_slug>[\w-]+)', views.article_by_category, name='article_by_category'),
    path('search/', views.search_results, name='search_results'),
    path('authors/', views.authors_index, name='authors_index'),
    re_path('authors/(?P<slug>[\w-]+)', views.authors_detail, name='authors_detail')
]
