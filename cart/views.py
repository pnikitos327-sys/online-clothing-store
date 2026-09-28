from django.shortcuts import get_object_or_404
from main.models import Product
from .services import add_to_cart
from django.contrib import redirect


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    add_to_cart(request, product)

    return redirect('card', slug=product.slug)