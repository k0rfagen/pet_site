from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('', views.ItemView.as_view()),
    path('cart/', views.CartView.as_view(), name='cart_view'),
    path('cart/add/<int:item_id>', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:item_id>', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
]
