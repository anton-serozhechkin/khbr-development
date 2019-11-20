from django.shortcuts import render
from .models import *

def main(request):
    context = []
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    context.append({'list_event': list_event})
    return render(request, 'event/index.html', locals())

def event_detail(request, *args, **kwargs):
    id_by_kwargs = kwargs.get('id')
    data_event = Event.objects.filter(id=id_by_kwargs)
    context = []
    context.append({'data_event': data_event})
    return render(request, 'event/event_detail.html', locals())