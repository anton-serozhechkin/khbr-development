from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth


def logout_view(request):
    logout(request)
    return redirect('analytics')

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
            print(user.email)
            print(user.username)
            print(user.password1)
            form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')            
            return redirect('analytics')
        else:
            form = SignUpUserForm()
    else:
        form = SignUpUserForm()
    return render(request, 'user/signup.html', locals())