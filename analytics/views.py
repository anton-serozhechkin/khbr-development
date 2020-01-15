from django.shortcuts import render
from .models import *

def main(request):
    context = []
    data_cat = Category.objects.filter(is_active=True)
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    context.append({'data_cat': data_cat, 'data_art': data_art, })
    return render(request, 'analytics/index.html', locals())


def article_detail(request, slug):
    data_art = Article.objects.filter(slug=slug)
    context = []
    context.append({'data_art': data_art})
    return render(request, 'analytics/article_detail.html', locals())