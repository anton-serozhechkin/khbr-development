from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from analytics.views import not_found_redirect

def main(request):
    context = []
    list_rait = Raiting.objects.filter(is_active=True).order_by('-created')
    context.append({'list_rait': list_rait})
    return render(request, 'raitings/index.html', locals())

    
def raiting_detail(request, slug):
    try:
        data_rait = get_object_or_404(Raiting, slug=slug)
    except:
        return redirect('404-not-found', kwargs={'name': 'рейтинг'})
    return render(request, 'raitings/raiting_detail.html', locals())