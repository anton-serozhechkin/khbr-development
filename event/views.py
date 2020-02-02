from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from analytics.views import not_found_redirect
from khbr.urls import not_found_redirect

def main(request):
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    context = {'list_event': list_event}
    return render(request, 'event/index.html', context)

def event_detail(request, slug):
    try:
        data_event = get_object_or_404(Event, slug=slug)
    except:
        return redirect('404-not-found', kwargs={'name': 'событие'})
    return render(request, 'event/event_detail.html', locals())