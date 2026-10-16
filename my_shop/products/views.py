from django.shortcuts import render,get_list_or_404
from products.models import Product,Effectiveness,Color_temperature
from products.utils import q_search


def catalog(request,category_slug=None):
    query=request.GET.get("q", None)
    on_sale=request.GET.get("on_sale", None)
    order_by=request.GET.get("order_by", None)

    if query:
        products=q_search(query)

    elif category_slug=="all":
        products=Product.objects.all()
        
    else:
        products=Product.objects.filter(category__slug=category_slug)

    if on_sale:
        products=products.filter(discounts__gt=0)
    
    if order_by and order_by!="default":
        products=products.order_by(order_by)

    products=get_list_or_404(products)

    context={
        "title":"Каталог",
        "products": products,
        'category_slug':category_slug
    }
    return render(request, 'products/catalog.html',context)


def product(request,product_slug):
    product=Product.objects.get(slug=product_slug)
    # effectiveness=Effectiveness.objects.all()
    # color_temperature=Color_temperature.objects.get()
    
    context={
    "title":"Продукт",
    "product":product,
    # "effectiveness":effectiveness,
    # "color_temperature":color_temperature
    }
    return render(request, 'products/product.html',context)

