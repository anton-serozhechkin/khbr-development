from django.shortcuts import render
from django.shortcuts import get_object_or_404

def main(request):
    return render(request, 'poll/index.html')

def poll_detail(request):
    return render(request, 'poll/poll_detail.html')