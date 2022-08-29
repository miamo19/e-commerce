
from django.urls import path
from .views import home, index, product_details, add_to_cart, cart, delete_cart

from shop import settings
urlpatterns = [
    path('', home, name="home"),
    path('index', index, name='index'),
    path('cart', cart, name='cart'),
    path('cart/delete', delete_cart, name='delete-cart'),
    path('products/<str:slug>/', product_details, name='products' ),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
]