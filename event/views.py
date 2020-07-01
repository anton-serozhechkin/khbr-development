from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from analytics.models import Article
from raitings.models import Raiting

def main(request):
    list_event = Event.objects.filter(is_active=True).order_by('-created')
    return render(request, 'event/index.html', locals())

def event_detail(request, slug):
    data_event = get_object_or_404(Event, slug=slug)
    event_images = EventImage.objects.filter(event__slug=slug)
    data_event.views += 1
    data_event.save()
    last_raitings = Raiting.objects.filter(is_active=True)[0:1]
    last_analytics = Article.objects.filter(is_active=True)[0:1]
    return render(request, 'event/event_detail.html', locals())