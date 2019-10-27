from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.contrib import messages

from .models import *
from .forms import ItemDetailsForm


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


# Choosing size and addons
def item_details(request, slug):
    form = ItemDetailsForm(request.POST or None)
    item = get_object_or_404(Item, slug=slug)
    item_info = {
        'user': request.user,
        'ordered': False,
        'item': item
    }
    if form.is_valid():
        item_info.update(form.cleaned_data)
        return add_to_cart(arg=item_info, request=request)
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'orders/itemDetails.html', context)


def add_to_cart(request, arg):
    order_item, created = OrderItem.objects.get_or_create(
        user=arg['user'],
        ordered=arg['ordered'],
        item=arg['item'],
        quantity=arg['quantity'],
        size=arg['size'],
        addon1=arg['addon1'],
        addon2=arg['addon2'],
        addon3=arg['addon3']
    )
    order_qs = Order.objects.filter(user=arg['user'])
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(id=order_item.id).exists():
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


def remove_from_cart(request, ajdi):
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = Order.objects.filter(user=request.user, ordered=False)[0]
        items = order.items.filter(id=ajdi)
        if items.exists():
            order.items.remove(items.first())
    return redirect('orders:cart')


def decrease_quantity(request, ajdi):
    item = get_item(request.user, ajdi)
    if item:
        item.quantity -= 1
        item.save()
    return redirect('orders:cart')


def increase_quantity(request, ajdi):
    item = get_item(request.user, ajdi)
    if item:
        item.quantity += 1
        item.save()
    return redirect('orders:cart')


def get_item(user, item_id):
    order_qs = Order.objects.filter(user=user, ordered=False)
    if order_qs.exists():
        item = order_qs.first().items.filter(id=item_id).first()
        return item
    return None
