from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from analytics.models import Subscribe, Article
from event.models import Event
from raitings.models import Raiting
@login_required(login_url='/user/signin/')
def personal_cabinet(request, private_data=None, change_password=None, unsubscribe=None, subscribe=None, links=None, delete_account=None):
    if Subscribe.objects.filter(email=request.user.email).exists():
        already_subscriber = True

    last_articles = Article.objects.filter(is_active=True)[0:3]
    last_events = Event.objects.filter(is_active=True)[0:2]
    last_raitings = Raiting.objects.filter(is_active=True)[0:1]

    fuck = True
    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "private_data'>>":
        private_data = True

    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "change_password'>>":
        change_password = True

    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "unsubscribe'>>":
        unsubscribe = True

    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "subscribe'>>":
        subscribe = True

    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "links'>>":
        links = True

    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "delete_account'>>":
        delete_account = True

    return render(request, 'personal_cabinet/index.html', locals())
