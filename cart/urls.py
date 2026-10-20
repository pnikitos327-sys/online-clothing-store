from django.urls import path
from .views import add_to_cart_view, views_cart

urlpatterns = [
    path('cart/add/<slug:slug>/', add_to_cart_view, name='add_to_cart'),
    path('cart/', views_cart, name='views_cart')
]