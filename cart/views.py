from django.shortcuts import get_object_or_404, redirect, render
from main.models import Product
from .servise import add_to_cart, get_cart
from .models import CartItem


def add_to_cart_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    add_to_cart(request, product)
    return redirect('views_cart')


def views_cart(request):
    cart = get_cart(request)
    products = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'products': products})
    
