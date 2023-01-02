from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.first, name='first'),
	path('about/', views.about, name='about'),
]