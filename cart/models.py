from django.db import models
from main.models import Product

class Cart(models.Model):
    session_key = models.CharField(max_length=255, unique=True)



    def __str__(self):
        return f"Корзина {self.session_key}"

from django.db import models

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('main.Product', on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"


