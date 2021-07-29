from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.encript_view, name='home'),
    path('encript_view', views.encript_view, name='home'),
    path('decript_view', views.decript_view, name='home')
]
