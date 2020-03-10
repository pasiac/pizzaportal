from django.urls import path

from .views import (MenuView, add_to_cart, cart, decrease_quantity,
                    increase_quantity, index, item_details, remove_from_cart)

app_name = "orders"

urlpatterns = [
    path("", index, name="home"),
    path("menu", MenuView.as_view(), name="menu"),
    path("add-to-cart/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<ajdi>", remove_from_cart, name="remove-from-cart"),
    path("cart", cart, name="cart"),
    path("details/<slug>", item_details, name="item_details"),
    path("decrease/<ajdi>", decrease_quantity, name="decrease-quantity"),
    path("increase/<ajdi>", increase_quantity, name="increase-quantity"),
]
