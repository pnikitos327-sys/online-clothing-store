from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
    list_display = ['session_key']

@admin.register(CartItem)
class CartItem_admin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']