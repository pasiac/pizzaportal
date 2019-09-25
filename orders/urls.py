from django.urls import path

from .views import index, MenuView, add_to_cart

app_name = "orders"

urlpatterns = [
    path("", index, name='home'),
    path("menu", MenuView.as_view(), name='menu'),
    path("add-to-cart/<name>/", add_to_cart, name='add-to-cart')
]
