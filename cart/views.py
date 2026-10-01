from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from main.models import Product
from .services import add_to_cart as service_add_to_cart

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    service_add_to_cart(request, product)
    return redirect('card', slug=product.slug)

    