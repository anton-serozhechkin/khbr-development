from django.contrib import admin
from django.urls import path, include
from analytics.views import not_found_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analytics.urls')),
    path('events/', include('event.urls')),
    path('videooverviews/', include('videooverview.urls')),
    path('raitings/', include('raitings.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('404-not-found', not_found_redirect, name='404-not-found')
]
