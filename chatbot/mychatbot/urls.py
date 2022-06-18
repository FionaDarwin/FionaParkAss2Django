from django.contrib import admin
from django.urls import path
from . import views
#the dot above means "from within the same directory"

urlpatterns = [
    path('', views.hi, name = 'home-page'),
]
