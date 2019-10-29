from django.shortcuts import render
from .models import *

def main(request):
    context = []
    data_cat = Category.objects.filter(is_active=True)
    data_art = Article.objects.filter(is_active=True)
    
    data_art_by_cat = Article.objects.filter()
    context.append({'data_cat': data_cat, 'data_art': data_art})
    return render(request, 'analytics/index.html', locals())


def article_by_categ(request, *args, **kwargs):
    print(*args)
    print(**kwargs)
    category_by_url = kwargs.get('slug')    
    data_art = Article.objects.filter(is_active=True, category=category_by_url)
    context = []
    context.append({'data_art': data_art})
    return render(request, 'analytics/article_by_categ.html', locals())


def article(request, *args, **kwargs):
    id_by_kwargs = kwargs.get('id')
    data_art = Article.objects.filter(id=id_by_kwargs)
    context = []
    context.append({'data_art': data_art})
    return render(request, 'analytics/article_detail.html', locals())