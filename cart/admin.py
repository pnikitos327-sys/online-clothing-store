from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class admin_art(admin.ModelAdmin):
    list_display = ['session_key']

@admin.register(CartItem)
class admin_cartitem(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity' ]