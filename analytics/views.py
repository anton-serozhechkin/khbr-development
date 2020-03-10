from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def main(request):
    data_cat = Category.objects.filter(is_active=True)
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    context = {'data_cat': data_cat, 'data_art': data_art}
    return render(request, 'analytics/index.html', context)


def article_detail(request, slug):
    data_art = get_object_or_404(Article, slug=slug)
    context = {'data_art': data_art}
    return render(request, 'analytics/article_detail.html', context)


def not_found_view(request, exception):
    return render(request, '404.html')

def error_view(request):
    return render(request, '500.html')

def permission_denied_view(request, exception):
    return render(request, '403.html')

def bad_request_view(request, exception):
    return render(request, '400.html')