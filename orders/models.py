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
    ("Peperoni", "Peperoni"), ("Sausage", "Sausage"), ("Mushrooms", "Mushrooms"),
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

    # def get_add_to_cart_url(self):
    #     return reverse("orders:item_details", kwargs={
    #         'slug': self.slug
    #     })




# Shopping cart
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=16, choices=(('S', 'Small'), ('L', 'Large')), default='S')
    addon1 = models.CharField(max_length=32, choices=ADDON_CHOICES, null=True, blank=True)
    addon2 = models.CharField(max_length=32, choices=ADDON_CHOICES, null=True, blank=True)
    addon3 = models.CharField(max_length=32, choices=ADDON_CHOICES, null=True, blank=True)

    # TODO: Get to know is it safe to pass such params this way
    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={
            'ajdi': self.id
        })

    def get_decrease_quantity_url(self):
        return reverse("orders:decrease-quantity", kwargs={
            'ajdi': self.id
        })

    def get_increase_quantity_url(self):
        return reverse("orders:increase-quantity", kwargs={
            'ajdi': self.id
        })

    def __str__(self):
        str = f'{self.quantity} {self.size} {self.item}'
        if self.addon1 != 'None' or self.addon2 != 'None' or self.addon3 != 'None':
            str += ' with'
        if self.addon1 != 'None':
            str += f' {self.addon1}'
        if self.addon2 != 'None':
            str += f' {self.addon2}'
        if self.addon3 != 'None':
            str += f' {self.addon3}'
        return str


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username




