from django.shortcuts import render , get_object_or_404
from . models import Product,Category
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,"home.html")

def product_list(request):
    products=Product.objects.filter( available=True)

    query=request.GET.get('q')

    category_slug =request.GET.get('category')

    if query:
        products=products.filter(
            Q(name__icontains=query)|
            Q(description__icontains=query)
        )
    if category_slug:
        products=products.filter(
            category__slug=category_slug
        )

    categories=Category.objects.all()

    return render(
        request,
        'products/product_list.html',{
            'products':products,
            'categories':categories,
            'query':query,
            'selected_category':category_slug,
            }
        )

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug,available=True)

    context={
        'product':product
    }

    return render(request,'products/product_detail.html',context)