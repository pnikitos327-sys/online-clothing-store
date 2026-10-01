from django.db import models
from main.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=255)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    