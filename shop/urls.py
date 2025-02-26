from django.contrib import admin
from django.urls import path, include

from shop import views
from shop.views import item_view

urlpatterns = [
    path('', item_view, name='mainpage'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:item_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('search/<str:search_body>', views.search, name='search_items' ),
]
