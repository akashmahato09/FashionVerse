from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        vendor = Vendor.objects.filter(
            email=email,
            password=password
        ).first()

        if vendor:
            request.session["vendor_id"] = vendor.id
            request.session["vendor_name"] = vendor.vendor_name

            messages.success(request, "Login successful.")
            return redirect("vendors:dashboard_page")

        else:
            messages.error(request, "Invalid email or password.")
            return redirect("vendors:login")

    return render(request, "vendors/login.html")

def register(request):
    if request.method == 'POST':
        vendor_name=request.POST.get("vendor_name")
        email=request.POST.get("email")
        phone_no=request.POST.get("mobile")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        profile_image = request.FILES.get("vendorProfile")

        if password==confirm_password:
           vendor=Vendor.objects.create(
               vendor_name=vendor_name,
               email=email,
               phone_no= phone_no,
               password=password,
               profile_image=profile_image
           )
           print("vendor registor succefull!")

           return redirect('vendors:login')
    return render(request, "vendors/register.html")

def dashboard_page(request):
    return render(request, "vendors/dashboard_page.html")

def profile(request):

    return render(request, "vendors/profile.html")

def products(request):

    vendor_id = request.session.get("vendor_id")

    if not vendor_id:
        return redirect("vendors:vendor_login")

    products = Product.objects.filter(
        vendor_id=vendor_id
    ).select_related("category").order_by("-created_at")

    context = {
        "products": products
    }

    return render(request, "vendors/products.html", context)

def delete_product(request, product_id):
    vendor_id = request.session.get("vendor_id")

    if not vendor_id:
        return redirect("vendors:vendor_login")

    product = get_object_or_404(
        Product,
        id=product_id,
        vendor_id=vendor_id
    )

    product.delete()

    return redirect("vendors:products")


def edit_product(request, product_id):

    vendor_id = request.session.get("vendor_id")

    if not vendor_id:
        return redirect("vendors:vendor_login")

    product = get_object_or_404(
        Product,
        id=product_id,
        vendor_id=vendor_id
    )

    categories = Category.objects.all()

    if request.method == "POST":

        product.category = Category.objects.get(
            id=request.POST.get("category")
        )

        product.product_name = request.POST.get("product_name")
        product.brand = request.POST.get("brand")
        product.description = request.POST.get("description")

        product.original_price = request.POST.get("original_price")
        product.selling_price = request.POST.get("selling_price")

        product.quantity = request.POST.get("quantity")
        product.stock_status = request.POST.get("stock_status")

        product.size = request.POST.get("size")
        product.color = request.POST.get("color")

        product.is_featured = "is_featured" in request.POST
        product.is_active = "is_active" in request.POST

        if request.FILES.get("product_image"):
            product.product_image = request.FILES["product_image"]

        product.save()

        return redirect("vendors:products")

    context = {
        "product": product,
        "categories": categories,
    }

    return render(request, "vendors/edit_product.html", context)

def add_product(request):
    vendor_id=request.session.get("vendor_id")
    vendor = Vendor.objects.get(id=vendor_id)
    category_id = request.session.get("category_id")

    category = Category.objects.get(id=category_id)

    if request.method == "POST":

        product_name = request.POST.get("productName")
        # category_id = request.POST.get("category")
        brand = request.POST.get("brand")
        description = request.POST.get("Product_disc")

        original_price = request.POST.get("original_price")
        selling_price = request.POST.get("selling_price")

        quantity = request.POST.get("product_quantity")

        stock_status = request.POST.get("stock_status")

        size = request.POST.get("size")
        color = request.POST.get("color")

        is_featured = request.POST.get("is_feature")
        is_active = request.POST.get("is_active")

        product_image = request.FILES.get("product_image")

        category = Category.objects.get(id=category_id)

        Product.objects.create(

            vendor=vendor,

            category=category,

            product_name =product_name,

            brand=brand,

            description=description,

            original_price=original_price,

            selling_price=selling_price,

            quantity=quantity,

            stock_status=stock_status,

            size=size,

            color=color,

            product_image=product_image,

            is_featured=is_featured,

            is_active=is_active,

        )
        print("PRODUCT SAVE SUCCESSFULLY!")

        return redirect("vendors:add_product")

    return render(request, "vendors/add_product.html", { "category":category} )

def orders(request):
    return render(request, "vendors/orders.html")

def customers(request):
    return render(request, "vendors/customers.html")

def reviews(request):
    return render(request, "vendors/reviews.html")

def coupons(request):
    return render(request, "vendors/coupons.html")

def notification(request):
    return render(request, "vendors/notification.html")

def earnings(request):
    return render(request, "vendors/earnings.html")

def reports(request):
    return render(request, "vendors/reports.html")

def settings(request):
    return render(request, "vendors/settings.html")

def product_category(request):
    return render(request, "vendors/product_category.html")

def category_men(request):
    if request.method == "POST":
        category, created = Category.objects.get_or_create(category_name="Men")
        if category:
            request.session["category_id"] = category.id
            return redirect('vendors:add_product')

def category_women(request):
    if request.method == "POST":
        category, created = Category.objects.get_or_create(category_name="Women")
        request.session["category_id"] = category.id
        if category:
            return redirect('vendors:add_product')

def category_boys(request):
    if request.method == "POST":
        category, created = Category.objects.get_or_create(category_name="Boys")
        if category:
            request.session["category_id"] = category.id
            return redirect('vendors:add_product')

def category_girls(request):
    if request.method == "POST":
        category, created = Category.objects.get_or_create(category_name="Girls")  
        if category:
            request.session["category_id"] = category.id
            return redirect('vendors:add_product')  

def category_kids(request):
    if request.method == "POST":
        category, created = Category.objects.get_or_create(category_name="Kids")  
        if category:
            request.session["category_id"] = category.id
            return redirect('vendors:add_product')      
           
      

