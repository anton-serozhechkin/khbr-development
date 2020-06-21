from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def main(request):
    polls = Poll.objects.filter(is_active=True).order_by('-created')
    return render(request, 'poll/index.html', locals())

def poll_detail(request, slug):
    poll = get_object_or_404(Poll, slug=slug)
    answers = Answer.objects.filter(poll__slug=slug)  
    return render(request, 'poll/poll_detail.html', locals())