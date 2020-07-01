from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from raitings.models import Raiting
from event.models import Event
from videooverview.models import VideoDownloading
from .forms import SubscribeForm
from django.db.models import Q

def main(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analytics')
        else:
            return redirect('analytics')
    else:
        form = SubscribeForm()
        last_art = Article.objects.filter(is_active=True).order_by('-created')[0:5]
        data_rait = Raiting.objects.filter(is_active=True).order_by('-created')[0:3]
        data_art_1_4 = Article.objects.filter(is_active=True)[0:3]
        data_video = VideoDownloading.objects.filter(is_active=True)[0:5]
        data_art_6_9 = Article.objects.filter(is_active=True)[5:8]
        data_event = Event.objects.filter(is_active=True)[0:3]
        integer_day = Article.objects.filter(integer_of_day=True).last()
    return render(request, 'analytics/index.html', locals())

def article_index(request):
    data_art = Article.objects.filter(is_active=True).order_by('-created')
    return render(request, 'analytics/article_index.html', locals())

def article_detail(request, category_slug, slug):
    article = get_object_or_404(Article, slug=slug)
    article_images = ArticleImage.objects.filter(article__slug=slug)
    article.views += 1
    article.save()
    last_raitings = Raiting.objects.filter(is_active=True)[0:1]
    last_events = Event.objects.filter(is_active=True)[0:1]

    try:
        next_article = article.get_next_by_created()
    except Exception:
        next_article=None

    try:
        previous_article = article.get_previous_by_created()
    except Exception:
        previous_article=None
    return render(request, 'analytics/article_detail.html', locals())

def article_by_category(request, category_slug):
    articles = Article.objects.filter(category__slug=category_slug, is_active=True).order_by('-created')
    category_name = Category.objects.get(slug=category_slug).name
    return render(request, 'analytics/article_by_category.html', locals())

def search_results(request):
    if request.GET.get('q'):
        query = request.GET.get('q')

        article_list = Article.objects.filter(
            Q(title__icontains=query)|
            Q(short_description__icontains=query)|
            Q(content__icontains=query)
        ).order_by('-created')
        
        event_list = Event.objects.filter(
            Q(title__icontains=query)|
            Q(short_description__icontains=query)|
            Q(content__icontains=query)
        ).order_by('-created')

        raiting_list = Raiting.objects.filter(
            Q(title__icontains=query)|
            Q(short_description__icontains=query)|
            Q(content__icontains=query)
        ).order_by('-created')
        
        video_list = VideoDownloading.objects.filter(
            Q(title__icontains=query)|
            Q(notes__icontains=query)
        ).order_by('-created')
        if not article_list or not event_list or not raiting_list or not video_list:
            answer = 'Ничего не найдено'
    else:    
        answer = 'Пустой запрос'

    return render(request, 'search/index.html', locals())

def authors_index(request):
    authors = Author.objects.all()
    return render(request, 'authors/index.html', locals())

def authors_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    return render(request, 'authors/author_detail.html', locals())

def not_found_view(request, exception):
    return render(request, 'errors/404.html')

def error_view(request):
    return render(request, 'errors/500.html')

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html')

def bad_request_view(request, exception):
    return render(request, 'errors/400.html')