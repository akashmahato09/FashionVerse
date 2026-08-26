from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from vendors.models import Product


class Order(models.Model):

    ORDER_STATUS = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Processing", "Processing"),
        ("Packed", "Packed"),
        ("Shipped", "Shipped"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
        ("Returned", "Returned"),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # Customer Details
    full_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=15)

    email = models.EmailField()

    # Shipping Address
    address_line_1 = models.CharField(max_length=255)

    address_line_2 = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    landmark = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    city = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    country = models.CharField(
        max_length=100,
        default="India"
    )

    pincode = models.CharField(max_length=6)

    order_status = models.CharField(
        max_length=30,
        choices=ORDER_STATUS,
        default="Pending"
    )

    ordered_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"