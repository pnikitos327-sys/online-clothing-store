from django.urls import path
from .views import add_to_cart

urlpatterns = [
    path('add/<slug:slug>/', add_to_cart, name='add_to_cart')
]
