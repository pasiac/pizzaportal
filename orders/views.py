from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView

from .models import *


# Create your views here.
def index(request):
    return render(request, "orders/index.html")


class MenuView(ListView):
    model = Item
    template_name = 'orders/menu.html'


def add_to_cart(request, name):
    item = get_object_or_404(Item, name=name)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__name=item.name).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)
    return redirect('orders:home')

