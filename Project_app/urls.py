from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('form', views.form,name='form'),
    path('table/', views.table,name='table'),
    path('updatetable/<id>', views.update_table,name='updatetable'),
    path('delete/<id>', views.delete,name='delete'),
]