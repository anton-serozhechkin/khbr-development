from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
    try:
        data_video = get_object_or_404(VideoView, slug=slug)
    except:
        return redirect('404-not-found', kwargs={'name': 'видео'})
    return render(request, 'videooverview/index.html', locals())
