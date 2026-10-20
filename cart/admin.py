from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class cart_admin(admin.ModelAdmin):
    list_display = ['session_key']

@admin.register(CartItem)
class cartItem_admin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity']