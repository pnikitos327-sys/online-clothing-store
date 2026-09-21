from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, db_index=True)
    brand = models.CharField(max_length=20, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(db_index=True, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    slug = models.SlugField(db_index=True, unique=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE  )
    image = models.ImageField(blank=True, null=True, upload_to='products/')
    is_main = models.BooleanField(default=True)


    def __str__(self):
        return f"картинка для {self.product.name}"