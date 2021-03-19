from django.urls import path
from . import views


urlpatterns = [
  path('', views.getHomeRoute, name="FirstView"),
  path('products/', views.getProducts, name="ProductList"),
  path('products/<str:pk>', views.getProduct, name="Product"),
]