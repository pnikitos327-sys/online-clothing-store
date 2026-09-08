from django.shortcuts import render
from .models import Product
 
def main(request):
    product = Product.objects.get(id=1)  
    return render(request, 'main.html', {'product': product}) 