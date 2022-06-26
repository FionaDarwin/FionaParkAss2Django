from django.contrib import admin
from django.urls import path
from . import views
#the dot above means "from within the same directory"
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #path('', views.hi, name = 'home-page'),
    path('', views.contact),
]

urlpatterns += staticfiles_urlpatterns()