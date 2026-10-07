from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("my-orders/", views.my_orders, name="my_orders"),
    path('shipping/<int:product_id>', views.shipping, name="shipping"),
    path('order-conform/', views.order_conform, name='order_conform'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),

]
