from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
	path('one_item/', views.one_item, name='one_item'),
]
