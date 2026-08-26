from django.urls import path
from . import views

app_name = "vendors"

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('profile/', views.profile, name='profile' ),
    path('products/', views.products, name='products'),
    path("delete-product/<int:product_id>/", views.delete_product, name="delete_product"),
    path("edit-product/<int:product_id>/", views.edit_product, name="edit_product"),
    path('add_product/', views.add_product, name='add_product'),
    path('orders/', views.orders, name='orders'),
    path('customers/', views.customers, name='customers'),
    path('reviews/', views.reviews, name='reviews'),
    path('coupons/', views.coupons, name='coupons'),
    path('notification/', views.notification, name='notification'),
    path('earnings/', views.earnings, name='earnings'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('product_category/', views.product_category, name='product_category'),
    path('category_men/', views.category_men, name="category_men"),
    path('category_women/', views.category_women, name='category_women'),
    path('category_boys/', views.category_boys, name='category_boys'),
    path('category_girls/', views.category_girls, name='category_girls'),
    path('category_kids/', views.category_kids, name='category_kids'),
    
    
    

]
