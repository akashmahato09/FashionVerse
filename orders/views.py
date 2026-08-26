from django.shortcuts import get_object_or_404, redirect, render
from orders.models import Order
from vendors.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order



# Create your views here.
@login_required
def my_orders(request):
    orders = Order.objects.filter(
        customer=request.user
    ).order_by("-ordered_at")

    return render(request, "orders/my_orders.html", {
        "orders": orders
    })

def shipping(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":

        quantity = int(request.POST.get("quantity"))
        total_price = product.selling_price * quantity

        Order.objects.create(
            customer=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price,

            full_name=request.POST.get("full_name"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
            address_line_1=request.POST.get("address_line_1"),
            address_line_2=request.POST.get("address_line_2"),
            landmark=request.POST.get("landmark"),
            city=request.POST.get("city"),
            district=request.POST.get("district"),
            state=request.POST.get("state"),
            country=request.POST.get("country"),
            pincode=request.POST.get("pincode"),
        )

        return redirect("payments:payment")

    context = {
        "product": product,
    }

    return render(request, "orders/shipping.html", context) 