from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#the dot above means "from within the same directory"

urlpatterns = [
    path('', views.hi, name = 'home-page'),
]

urlpatterns += staticfiles_urlpatterns()