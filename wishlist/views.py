from itertools import product
from urllib import request
from django.db.models.aggregates import Sum
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from .models import Product,Wishlist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#================= Wishlist Page =========================

@login_required
def mywishlist(request):

    wishlist_items = Wishlist.objects.filter(
        user=request.user
    ).select_related("product")

    num_of_items = (
           Cart.objects.filter(user=request.user)
           .aggregate(total=Sum("quantity"))["total"] or 0
       )
    print("total nums of items:", num_of_items)
    context = {

        "wishlist_items": wishlist_items,
        "num_of_items":num_of_items,

    }

    return render(
        request,
        "wishlist/mywishlist.html",
        context
    )

#================ Add Wishlist ===================

@login_required
def add_wishlist(request,id):

    product = get_object_or_404(Product,id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect(request.META.get("HTTP_REFERER"))




#================ Remove Wishlist ===================

@login_required
def remove_wishlist(request,id):

    product = get_object_or_404(Product,id=id)

    Wishlist.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect("core:wishlist")





