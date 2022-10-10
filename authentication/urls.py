from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = [
    path('signup/',views.signup),
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]