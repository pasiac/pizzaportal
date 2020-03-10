from django.contrib import admin

from .models import *

admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(UserCart)
admin.site.register(Category)
admin.site.register(Topping)
admin.site.register(Deliverymen)
