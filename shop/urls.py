from django.contrib import admin
from django.urls import path, include

from shop import views
from shop.views import item_view, RegisterView, email_send_test

app_name = "shop"
urlpatterns = [
    path("", item_view, name="mainpage"),
    path('404', views.error404, name="error404"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/add/<int:item_id>", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:item_id>", views.remove_from_cart, name="remove_from_cart"),
    path("search/", views.search, name="search"),
    path("item/<int:item_id>", views.item_card, name="item_card"),
    path("cart/minus/<int:item_id>", views.minus, name="minus_one"),
    path("cart/plus/<int:item_id>", views.plus, name="plus_one"),
    path("contacts/", views.contacts, name="contacts"),
    path("profile/", views.profile, name="profile"),
    path("accounts/register", RegisterView.as_view(), name="register"),
    path('uploadnewitem/', views.add_item, name="upload_new_item"),
]
