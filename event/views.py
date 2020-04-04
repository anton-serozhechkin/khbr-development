from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def main(request):
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    if list_event:
        context = {'list_event': list_event}
    else:
        context = {'blank': 'К сожалению, ничего не найдено'}
    return render(request, 'event/analytic_detail.html', context)

def event_detail(request, slug):
    data_event = get_object_or_404(Event, slug=slug)
    context = {'data_event': data_event}
    return render(request, 'event/event_detail.html', context)