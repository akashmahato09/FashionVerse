from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from vendors.models import Product
from .models import Cart

# Create your views here.

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart_item, created = Cart.objects.get_or_create(

        user=request.user,

        product=product

    )

    if not created:

        cart_item.quantity += 1

        cart_item.save()

   

    return redirect("cart:cart_page")

@login_required
def cart_page(request):

    cart_items = Cart.objects.filter(
        user=request.user
    )

    total = sum(item.total_price for item in cart_items)
    num_of_items = (
        Cart.objects.filter(user=request.user)
        .aggregate(total=Sum("quantity"))["total"] or 0
    )
    request.session["num_of_items"] = num_of_items

    

    return render(
        request,
        "cart/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
            "num_of_items":num_of_items,
        }
    )

@login_required
def remove_cart(request, cart_id):

    cart = get_object_or_404(
        Cart,
        id=cart_id,
        user=request.user
    )

    cart.delete()

    return redirect("cart:cart_page")