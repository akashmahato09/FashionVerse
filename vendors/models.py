from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# ===========================Vendor register ================================================
class Vendor(models.Model):

    vendor_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone_no = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )
    profile_image = models.ImageField(
        upload_to="vendors/profile/",
        blank=True,
        null=True,
        default="vendors/profile/default.png"   # Optional
    )

    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name



# ==================================Product Area =====================================

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    STOCK_STATUS = (
        ("In Stock", "In Stock"),
        ("Out of Stock", "Out of Stock"),
    )

    SIZE_CHOICES = (
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
        ("XXL", "XXL"),
    )

    COLOR_CHOICES = (
        ("Black", "Black"),
        ("White", "White"),
        ("Blue", "Blue"),
        ("Red", "Red"),
        ("Green", "Green"),
        ("Yellow", "Yellow"),
        ("Pink", "Pink"),
        ("Grey", "Grey"),
    )

    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    product_name = models.CharField(max_length=200)

    brand = models.CharField(max_length=100, blank=True)

    description = models.TextField()

    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    stock_status = models.CharField(
        max_length=20,
        choices=STOCK_STATUS,
        default="In Stock"
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        blank=True,
        null=True
    )

    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        blank=True,
        null=True
    )

    product_image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def discount_percentage(self):
        if self.original_price > self.selling_price:
            return round(
                ((self.original_price - self.selling_price)
                 / self.original_price) * 100
            )
        return 0

    def __str__(self):
        return self.product_name






    
