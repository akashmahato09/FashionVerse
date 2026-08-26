from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404, render
from cart.models import Cart
from vendors.models import *

# Create your views here.
def index(request):
    product=Product.objects.all();
   
    # num_of_items = (
    #     Cart.objects.filter(user=request.user)
    #     .aggregate(total=Sum("quantity"))["total"] or 0
    # )
    # print("total nums of items:", num_of_items)
    context={
        "product":product,
    }
    return render(request, "core/index.html", context)

def men(request):
   products = Product.objects.filter(
        category__category_name="Men",
        is_active=True
    )
#    num_of_items = (
#         Cart.objects.filter(user=request.user)
#         .aggregate(total=Sum("quantity"))["total"] or 0
#     )
#    print("total nums of items:", num_of_items)
       

   return render(request, "core/men.html", {
        "products": products,
    })

def women(request):
    products = Product.objects.filter(
        category__category_name="Women",
        is_active=True
    )
    
    return render(request, "core/women.html", {
        "products": products,
         
    })

def boys (request):
    products = Product.objects.filter(
        category__category_name="Boys",
        is_active=True
    )
     
    return render(request, "core/boys.html", {
        "products": products,
         
    })

def girls(request):
    products = Product.objects.filter(
        category__category_name="Girls",
        is_active=True
    )
     
    return render(request, "core/girls.html", {
        "products": products,
         
    })
def kids(request):
    products = Product.objects.filter(
        category__category_name="Kids",
        is_active=True
    )
     

    return render(request, "core/kids.html", {
        "products": products,
         
    })

def products_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
     
    context = {
        "product": product,
         
    }

    return render(request, "core/products_details.html", context)
