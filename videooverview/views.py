from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from analytics.views import not_found_redirect

def main(request):
    list_videos = Video.objects.filter(is_active=True).order_by('-created')
    context = {'list_videos': list_videos}
    return render(request, 'videooverview/index.html', context)

def video_detail(request, slug):
    try:
        data_video = get_object_or_404(Video, slug=slug)
    except:
        return redirect('404-not-found', kwargs={'name': 'видео'})
    return render(request, 'videooverview/video_detail.html', locals())
