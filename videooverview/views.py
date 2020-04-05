from django.shortcuts import render
from .models import *

def main(request):
    data_video = VideoDownloading.objects.filter(is_active=True)
    
    if data_video:
        context = {'data_video': data_video}
    else:
        context = {'blank': 'К сожалению, ничего не найдено'}
    return render(request, 'videooverview/analytic_detail.html', context)
