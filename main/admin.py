from django.contrib import admin
from .models import Product, Category, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ['image', 'is_main']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'brand', 'category']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'brand']
    prepopulated_fields = {'slug' : ('name',)}
    inlines = [ProductImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug' : ('name',)}


