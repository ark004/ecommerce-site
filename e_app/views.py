from django.shortcuts import get_object_or_404, render
from .models import Category, Product

# Create your views here.



def all_products (request):
    products=Product.product.all()
    return render(request,'index.html',{'products':products})

def product_detail (request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request,'singles.html',{'product':product})

def category(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    Products = Product.objects.filter(category = category)
    return render(request,'category.html',{'category':category, 'products':Products})




