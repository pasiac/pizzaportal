from django.urls import path

from .views import index, MenuView, add_to_cart, remove_from_cart, cart

app_name = "orders"

urlpatterns = [
    path("", index, name='home'),
    path("menu", MenuView.as_view(), name='menu'),
    path("add-to-cart/<slug>/", add_to_cart, name='add-to-cart'),
    path("remove-from-cart/<slug>&<delete>/", remove_from_cart, name='remove-from-cart'),
    path("cart", cart, name='cart')
]
