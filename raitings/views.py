from django.shortcuts import render
from .models import *

def main(request):
    context = []
    list_rait = Raiting.objects.filter(is_active=True).order_by('-created')
    context.append({'list_rait': list_rait})
    return render(request, 'raitings/index.html', locals())

    
def raiting_detail(request, *args, **kwargs):
    id_by_kwargs = kwargs.get('id')
    data_rait = Raiting.objects.filter(id=id_by_kwargs)
    context = []
    context.append({'data_rait': data_rait})
    return render(request, 'raitings/raiting_detail.html', locals())