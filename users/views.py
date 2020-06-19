from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth
from analytics.models import Subscribe

def logout_view(request):
    logout(request)
    return redirect('analytics')

def recovery(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
    return render(request, 'user/recovery.html', locals())

def signin(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('analytics')
        else:
            return redirect('signin')
    return render(request, 'user/signin.html', locals())

def signup(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.email = form.cleaned_data.get('email')
            user.username = form.cleaned_data.get('username')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            try:
                subscribe = request.POST['subscribe']
                new_subscriber = Subscribe.objects.create(email=user.email)
                new_subscriber.save()
            except:
                pass
            
            form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')            
            return redirect('analytics')
        else:
            form = SignUpUserForm()
    else:
        form = SignUpUserForm()
    return render(request, 'user/signup.html', locals())