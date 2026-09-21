from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def main(request):
    products = Product.objects.all()
    return render(request, 'main.html', {'products': products})


def card(request, slug):
    product = get_object_or_404(Product, slug=slug)
    main_image = product.images.filter(is_main=True).first()
    return render(request, 'card.html', {'product': product, 'main_image': main_image})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})