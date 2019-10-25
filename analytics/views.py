from django.shortcuts import render
from .models import *

def main(request):
    context = []
    data_cat = Category.objects.all()
    data_art = Article.objects.all()
    context.append({'data_cat': data_cat, 'data_art': data_art})
    print(context)
    return context

def show_categ(request):
    data_cat = Category.objects.filter(is_active=True)
    context = []
    context.append({'data_cat': data_cat})
    print(context)
    return context