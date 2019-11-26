from django.shortcuts import render
from .models import *

def main(request, *args, **kwargs):
    print(*args)
    print(**kwargs)
    context = []
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    context.append({'list_event': list_event})
    return render(request, 'event/index.html', locals())

def event_detail(request, id):
    data_event = Event.objects.filter(id=id)
    context = []
    context.append({'data_event': data_event})
    return render(request, 'event/event_detail.html', locals())