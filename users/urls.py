from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('sign-out/', views.logout_view, name='sign_out'),
    path('recovery/', views.recovery, name='recovery'),
]
