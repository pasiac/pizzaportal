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


# If delete == True it will completely delete item from cart
# else it will decrease quantity or delete if quantity will be 0
# TODO:
# I dont know why it doesnt delete order_item entry when orders
# quantity equal 0, but if delete equal True it does with same code used
def remove_from_cart(request, slug, delete):
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
            if delete == 'True':
                order.items.remove(order_item)
                order_item.delete()
                messages.info(request, "This item was removed from your cart.")
            else:
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    messages.info(request, "Quantity updated.")
                else:
                    order.items.remove(order_item)
                    order_item.delete()
                    messages.info(request, "This item was removed from your cart.")
            order_item.save()
            order.save()
            return redirect("orders:cart")
        else:
            # return orders:menu
            messages.info(request, "This item was not in your cart")
            return redirect("orders:menu")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("orders:menu")

