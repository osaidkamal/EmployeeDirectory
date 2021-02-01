from django.contrib import admin
from django.contrib.auth.forms import UsernameField
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import show, details
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('registerhidden/', views.registerhidden, name="registerhidden"),
    path('logout/', views.logoutas, name="logout"),
    path('login/', views.loginas, name="login"),
    path('details/<str:pk>/', views.details, name='details'),
    path('show/<str:pk>/', views.show, name="show"),
    path('update/<str:pk>/', views.update, name="update"),
] 
