from django.shortcuts import render
from .models import *

def main(request):
    data_cat = Category.objects.filter()
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    latest = Article.objects.order_by('-created')[0:3]
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get("email")
            new_signup = Signup()
            new_signup.email = email
            new_signup.save()
        else:
            error = 'Убедитесь в том, что введеный адрес почты валиден'
    context = {
        'data_cat': data_cat, 
        'data_art': data_art,
        'latest': latest
        }
    return render(request, 'analytics/index.html', context)


def article_detail(request, slug):
    data_art = Article.objects.filter(slug=slug)
    context = []
    context.append({'data_art': data_art})
    return render(request, 'analytics/article_detail.html', locals())