from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.db.models import ManyToManyField
from django.urls import reverse


class UserCart(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = ManyToManyField("CartItem")
    placed_date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def calculate_value(self):
        # Narazie zeruje potem dorobie
        self.value = 0
        for item in self.items.all():
            if item.size == "Small":
                self.value += item.item.small_price * item.quantity
            else:
                self.value += item.item.large_price * item.quantity
            for topping in item.topping.all():
                self.value += topping.price
        self.save()


class CartItem(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(
        max_length=8, choices=[("S", "Small"), ("L", "Large")], default="Small"
    )
    topping = models.ManyToManyField("Topping")

    # TODO: Get to know is it safe to pass such params this way
    def get_remove_from_cart_url(self):
        return reverse("orders:remove-from-cart", kwargs={"ajdi": self.id})

    def get_decrease_quantity_url(self):
        return reverse("orders:decrease-quantity", kwargs={"ajdi": self.id})

    def get_increase_quantity_url(self):
        return reverse("orders:increase-quantity", kwargs={"ajdi": self.id})

    def __str__(self):
        return f"{self.item.name}  sztuk: {self.quantity}  wielkosci: {self.size} dodatek: {self.topping.first()}"


class Item(models.Model):
    name = models.CharField(max_length=20)
    small_price = models.FloatField()
    large_price = models.FloatField(null=True, blank=True)
    slug = models.SlugField(max_length=6)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(default="2.00")

    def __str__(self):
        return self.name


class Deliverymen(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.second_name
