from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from analytics.models import Subscribe, Article
from event.models import Event
from raitings.models import Raiting
from django.contrib.auth.models import User


@login_required(login_url='/user/signin/')
def personal_cabinet(request, news=None, private_data=None, change_password=None, subscribe=None, unsubscribe=None, links=None):
    if Subscribe.objects.filter(email=request.user.email).exists():
        already_subscriber = True
    
    if news:
        last_articles = Article.objects.filter(is_active=True).order_by('-created')[0:2]
        last_events = Event.objects.filter(is_active=True).order_by('-created')[0:2]
        last_raitings = Raiting.objects.filter(is_active=True).order_by('-created')[0:1]

    if private_data:
        if request.method == "POST":
            if request.POST['personal_user_name']:
                change_name = User.objects.get(username=request.user.username)
                change_name.username = request.POST['personal_user_name']
                change_name.save()
            if request.POST['personal_user_email']:
                change_email = User.objects.get(username=request.user.username)
                change_email.email = request.POST['personal_user_email']
                change_email.save()
            return redirect('personal_cabinet')

    if change_password:
        if request.method == "POST":
            if request.POST['personal_user_password'] and request.POST['personal_user_confirmationPassword']:
                if request.POST['personal_user_password'] == request.POST['personal_user_confirmationPassword']:
                    change_password_form = User.objects.get(username=request.user.username)
                    change_password_form.set_password(request.POST['personal_user_password'])
                    change_password_form.save()
                else:
                    error = 'Пароли не совпадают. Попробуйте еще раз.'
            else:
                error = 'Заполните все поля формы и попробуйте еще раз.'

    if unsubscribe:
        if request.method == "POST":
            Subscribe.objects.filter(email=request.user.email).delete()
            return redirect('subscribe')
    
    if subscribe:
        if request.method == "POST":
            if Subscribe.objects.filter(email=request.POST['personal_user_subscribe']).exists():
              error = 'Этот email уже подписан на рассылку'
            else:  
                Subscribe.objects.create(email=request.POST['personal_user_subscribe'])            
                return redirect('unsubscribe')

    return render(request, 'personal_cabinet/index.html', locals())
