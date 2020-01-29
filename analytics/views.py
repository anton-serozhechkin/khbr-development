from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def main(request):
    data_cat = Category.objects.filter()
    data_art = Article.objects.filter(is_active=True).order_by('-created')[:6]
    latest = Article.objects.order_by('-created')[0:3]
    context = {
        'data_cat': data_cat, 
        'data_art': data_art,
        'latest': latest,
        }
    if request.method == "POST":
        if form.is_valid():
            email = request.POST.get("email")
            new_signup = Signup()
            new_signup.email = email
            new_signup.save()
        else:
            error = 'Убедитесь в том, что введеный адрес почты валиден'
            context = {'error': error}
    
    return render(request, 'analytics/index.html', context)


def article_detail(request, slug):
    try:
        data_art = get_object_or_404(Article, slug=slug)
    except:
        return redirect('404-not-found', kwargs={'name': 'пост'})
    return render(request, 'analytics/article_detail.html', locals())

def not_found_redirect(request, **kwargs):
    print(**kwargs)
    name = '**kwargs('
    return render(request, '404.html', name)