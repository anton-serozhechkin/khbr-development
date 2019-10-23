from django.shortcuts import render
from models import Category

def main(request):
    data = Category.objects.all()
    return data

