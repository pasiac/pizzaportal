from django.db import models
from django.conf import settings
from django.urls import reverse

CATEGORY_CHOICES = (
    ("S", "Salad"),
    ("SU", "Subs"),
    ("SP", "Sicilian Pizza"),
    ("RP", "Regular Pizza"),
    ("DP", "Dinner Plate"),
    ("P", "Pasta")
)

ADDON_CHOICES = (
    ("Peperoni", "Peperoni"), ("None", "None"), ("Sausage", "Sausage"), ("Mushrooms", "Mushrooms"),
    ("Onions", "Onions"),
    ("Canadian Bacon", "Canadian Bacon"), ("Pineapple", "Pineapple"), ("Eggplant", "Eggplant"),
    ("Tomato & Basil", "Tomato & Basil"), ("Green Peppers", "Green Peppers"), ("Hamburger", "Hamburger"),
    ("Spinach", "Spinach"), ("Zucchini", "Zucchini"), ("Ham", "Ham"), ("Fresh Garlic", "Fresh Garlic"),
    ("Artichoke", "Artichoke"), ("Buffalo Chicken", "Buffalo Chicken"), ("Barbecue Chicken", "Barbecue Chicken"),
    ("Anchovies", "Anchovies"), ("Black Olives", "Black Olives")
)


class Item(models.Model):
    name = models.CharField(max_length=32)
    small_price = models.FloatField()
    large_price = models.FloatField(null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("orders:add-to-cart", kwargs={
            'slug': self.slug
        })

    # TODO: Get to know is it safe to pass such params this way
    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={
            'slug': self.slug,
            'delete': True
        })

    def get_decrease_quantity_url(self):
        return reverse("orders:remove-from-cart", kwargs={
            'slug': self.slug,
            'delete': False
        })


# Shopping cart
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=16, choices=(('S', 'Small'), ('L', 'Large')), default='S')
    addon1 = models.CharField(max_length=32, choices=ADDON_CHOICES, default='None')
    addon2 = models.CharField(max_length=32, choices=ADDON_CHOICES, default='None')
    addon3 = models.CharField(max_length=32, choices=ADDON_CHOICES, default='None')

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




