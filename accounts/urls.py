from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
