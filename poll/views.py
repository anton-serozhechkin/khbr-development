from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.contrib.auth.models import User
 

def main(request):
    polls = Poll.objects.filter(is_active=True).order_by('-created')
    return render(request, 'poll/index.html', locals())

def poll_detail(request, slug):
    poll = get_object_or_404(Poll, slug=slug)
    answers = Answer.objects.filter(poll__slug=slug)
    if request.user.is_authenticated and UserAnswer.objects.filter(user__username=request.user.username, poll__slug=slug).exists():
            user_took_part = True
    #if request.method == 'POST':
    print(request.method)


      
    return render(request, 'poll/poll_detail.html', locals())