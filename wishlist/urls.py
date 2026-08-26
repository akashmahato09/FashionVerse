from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path("", views.mywishlist, name="mywishlist"),
    path("add/<int:id>/", views.add_wishlist, name="add_wishlist"),
    path("remove/<int:id>/", views.remove_wishlist, name="remove_wishlist"),
]