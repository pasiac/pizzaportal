from django.db import models
from django.conf import settings


# class Addons(models.Model):
#     name = models.TextField(max_length=32)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#
#     def __str__(self):
#         return self.name
#
#
# class Toppings(models.Model):
#     TOPPINGS = (
#         ("Peperoni", "Peperoni"), ("None", "None"), ("Sausage", "Sausage"), ("Mushrooms", "Mushrooms"),
#         ("Onions", "Onions"),
#         ("Canadian Bacon", "Canadian Bacon"), ("Pineapple", "Pineapple"), ("Eggplant", "Eggplant"),
#         ("Tomato & Basil", "Tomato & Basil"), ("Green Peppers", "Green Peppers"), ("Hamburger", "Hamburger"),
#         ("Spinach", "Spinach"), ("Zucchini", "Zucchini"), ("Ham", "Ham"), ("Fresh Garlic", "Fresh Garlic"),
#         ("Artichoke", "Artichoke"), ("Buffalo Chicken", "Buffalo Chicken"), ("Barbecue Chicken", "Barbecue Chicken"),
#         ("Anchovies", "Anchovies"), ("Black Olives", "Black Olives")
#     )
#     item1 = models.TextField(max_length=16, null=True, blank=True, choices=TOPPINGS)
#     item2 = models.TextField(max_length=16, null=True, blank=True, choices=TOPPINGS)
#     item3 = models.TextField(max_length=16, null=True, blank=True, choices=TOPPINGS)
#
#     def __str__(self):
#         return f'{self.item1}, {self.item2}, {self.item3}'
#
#
# class Pizza(models.Model):
#     name = models.TextField(max_length=32)
#     small_price = models.DecimalField(max_digits=4, decimal_places=2)
#     large_price = models.DecimalField(max_digits=4, decimal_places=2)
#     toppings = models.ForeignKey(Toppings, on_delete=models.CASCADE) #to wywala program
#     regular = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Sub(models.Model):
#     name = models.TextField(max_length=32)
#     small_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     large_price = models.DecimalField(max_digits=4, decimal_places=2)
#     # addon = models.OneToOneField(Addons, on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return self.name
#
#
# class Pasta(models.Model):
#     name = models.TextField(max_length=32)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#
#     def __str__(self):
#         return self.name
#
#
# class Salad(models.Model):
#     name = models.TextField(max_length=32)
#     price = models.DecimalField(max_digits=4, decimal_places=2)
#
#     def __str__(self):
#         return self.name
#
#
# class DinnerPlatters(models.Model):
#     name = models.TextField(max_length=32)
#     small_price = models.DecimalField(max_digits=4, decimal_places=2)
#     large_price = models.DecimalField(max_digits=4, decimal_places=2)
#
#     def __str__(self):
#         return self.name
from django.urls import reverse

CATEGORY_CHOICES = (
    ("S", "Salad"),
    ("SU", "Subs"),
    ("SP", "Sicilian Pizza"),
    ("RP", "Regular Pizza"),
    ("DP", "Dinner Plate"),
    ("P", "Pasta")
)


class Item(models.Model):
    name = models.CharField(max_length=32)
    small_price = models.FloatField()
    large_price = models.FloatField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def get_add_to_cart_url(self):
        return reverse("orders:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={
            'slug': self.slug
        })


# Shopping cart
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username




