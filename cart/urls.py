from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [

    path(
        "add/<int:product_id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),

    path(
        "",
        views.cart_page,
        name="cart_page"
    ),

    path(
        "remove/<int:cart_id>/",
        views.remove_cart,
        name="remove_cart"
    ),

]