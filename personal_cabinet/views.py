from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from analytics.models import Subscribe

@login_required(login_url='/user/signin/')
def personal_cabinet(request, private_data=None, change_password=None, unsubscribe=None, subscribe=None, links=None, delete_account=None):
    if Subscribe.objects.filter(email=request.user.email).exists():
        already_subscriber = True
    if str(request.build_absolute_uri).rsplit('/', 1)[-1] == "private_data'>>":
        print('da')
    print(str(request.build_absolute_uri).rsplit('/', 1)[-1])
    return render(request, 'personal_cabinet/index.html', locals())
