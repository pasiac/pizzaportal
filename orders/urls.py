from django.urls import path

from .views import index, MenuView, add_to_cart, remove_from_cart, cart,\
    item_details, decrease_quantity, increase_quantity

app_name = "orders"

urlpatterns = [
    path("", index, name='home'),
    path("menu", MenuView.as_view(), name='menu'),
    path("add-to-cart/", add_to_cart, name='add-to-cart'),
    path("remove-from-cart/<ajdi>", remove_from_cart, name='remove-from-cart'),
    path("cart", cart, name='cart'),
    path("<str:slug>/details", item_details, name='item_details'),
    path("decrease/<ajdi>", decrease_quantity, name='decrease-quantity'),
    path("increase/<ajdi>", increase_quantity, name='increase-quantity')
]
