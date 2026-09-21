from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('card/<slug:slug>/', views.card, name='card'),
    path('category/<slug:slug>/', views.category, name='category'), 
]