from django.urls import path
from . import views

app_name="core"

urlpatterns = [
    path('', views.index, name='home'),
    path('men', views.men, name='men'),
    path('women', views.women, name='women'),
    path('boys', views.boys, name='boys'),
    path('girls', views.girls, name='girls'),
    path('kids', views.kids, name='kids'),
    path("products_details/<int:product_id>/", views.products_details, name="products_details"),
]
 