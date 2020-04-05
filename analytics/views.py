from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def main(request):
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    if data_art:
        context = {'data_art': data_art}
    else:
        context = {'blank': 'К сожалению, ничего не найдено'}
    return render(request, 'analytics/index.html', context)

def article_index(request):
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    if data_art:
        context = {'data_art': data_art}
    else:
        context = {'blank': 'К сожалению, ничего не найдено'}
    return render(request, 'analytics/article_index.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'analytics/article_detail.html', locals())

def not_found_view(request, exception):
    return render(request, '404.html')

def error_view(request):
    return render(request, '500.html')

def permission_denied_view(request, exception):
    return render(request, '403.html')

def bad_request_view(request, exception):
    return render(request, '400.html')
