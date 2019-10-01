from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.contrib import messages

from .models import *


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


# Class view
class MenuView(ListView):
    model = Item
    template_name = 'orders/menu.html'


def cart(request):
    context = {
        'order': Order.objects.filter(user=request.user, ordered=False)
    }
    return render(request, 'orders/cart.html', context)


# It would fix code duplication
def get_order(request, slug):
    pass


# If add to cart button is clicked it add item to cart
# or if it is already in cart it increase its quantity
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # get_or_create returns tuple returns object and boolean true if created
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to cart")
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)
        messages.info(request, "Item added to cart")
    return redirect('orders:cart')


# It will completely delete item from cart
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # Get users orders
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        # Get user cart
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            for item in order.items.all():
                if item == order_item:
                    item.delete()
            messages.info(request, "This item was removed from your cart.")
            order.save()
            return redirect("orders:home")
        else:
            # return orders:menu
            messages.info(request, "This item was not in your cart")
            return redirect("orders:menu")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("orders:menu")


# This will decrease quantity of selected item
# Probably I should create function to get order and ordered_item
# to avoid code duplication
def decrease_quantity(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # Get users orders
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        # Get user cart
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            for item in order.items.all():
                if item == order_item:
                    item.quantity -= 1
            messages.info(request, "Quantity updated.")
            order.save()
            return redirect("orders:cart")
    else:
        messages.info(request, "You dont have an active order")
        return redirect("orders:menu")


# Its increase quantity also have to fix code duplication
def increase_quantity(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # Get users orders
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        # Get user cart
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            for item in order.items.all():
                if item == order_item:
                    item.quantity += 1
            messages.info(request, "Quantity updated")
            order.save()
            return redirect("orders:cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("orders:menu")
