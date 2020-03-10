from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import ItemDetailsForm
from .models import *


def index(request):
    return render(request, "orders/index.html")


class MenuView(ListView):
    model = Item
    template_name = "orders/menu.html"


def cart(request):
    context = {"order": UserCart.objects.filter(user=request.user, completed=False)}
    return render(request, "orders/cart.html", context)


def item_details(request, slug):
    item = get_object_or_404(Item, slug=slug)
    form = ItemDetailsForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data.update({"item": item})
        return add_to_cart(request=request, cart_item_data=form.cleaned_data)

    return render(request, "orders/itemDetails.html", {"form": form, "item": item})


def add_to_cart(request, cart_item_data):
    item_to_add = __create_cart_item(cart_item_data)
    user_cart, was_created = UserCart.objects.get_or_create(
        user=request.user, completed=False,
    )
    if was_created:
        user_cart.items.add(item_to_add)
    else:
        cart_item = user_cart.items.filter(
            item__name=item_to_add.item.name,
            size=item_to_add.size,
            topping=item_to_add.topping.first(),
        ).first()
        if cart_item:
            cart_item.quantity = item_to_add.quantity
        else:
            user_cart.items.add(item_to_add)
    user_cart.calculate_value()
    return redirect("orders:cart")


def __create_cart_item(cart_item_data: dict) -> CartItem:
    # Będzie działać dla jednego dodatku
    topping = cart_item_data.pop("topping")[0]
    cart_item = CartItem.objects.filter(
        item=cart_item_data["item"], size=cart_item_data["size"], topping=topping
    ).first()

    if not cart_item:
        cart_item = CartItem.objects.create(**cart_item_data)
        cart_item.topping.add(topping)
    else:
        cart_item.quantity += cart_item_data["quantity"]
    cart_item.save()
    return cart_item


def remove_from_cart(request, ajdi):
    order_qs = UserCart.objects.filter(user=request.user)
    if order_qs.exists():
        order = UserCart.objects.filter(user=request.user, completed=False)[0]
        items = order.items.filter(id=ajdi)
        if items.exists():
            order.items.remove(items.first())
    return redirect("orders:cart")


def decrease_quantity(request, ajdi):
    item = get_item(request.user, ajdi)
    if item:
        item.quantity -= 1
        item.save()
    return redirect("orders:cart")


def increase_quantity(request, ajdi):
    item = get_item(request.user, ajdi)
    if item:
        item.quantity += 1
        item.save()
    return redirect("orders:cart")
