# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('products/', views.product_list, name='product_list'),  # Product list page
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Product detail page
    path('buy-now/<int:pk>/', views.buy_now, name='buy_now'),  # Buy now page
]
