from django.db import models


class Topping(models.Model):
    TOPPINGS = (
        ("Peperoni", "Peperoni"), ("Sausage", "Sausage"), ("Mushrooms", "Mushrooms"), ("Onions", "Onions"),
        ("Canadian Bacon", "Canadian Bacon"), ("Pineapple", "Pineapple"), ("Eggplant", "Eggplant"),
        ("Tomato & Basil", "Tomato & Basil"), ("Green Peppers", "Green Peppers"), ("Hamburger", "Hamburger"),
        ("Spinach", "Spinach"), ("Zucchini", "Zucchini"), ("Ham", "Ham"), ("Fresh Garlic", "Fresh Garlic"),
        ("Artichoke", "Artichoke"), ("Buffalo Chicken", "Buffalo Chicken"), ("Barbecue Chicken", "Barbecue Chicken"),
        ("Anchovies", "Anchovies"), ("Black Olives", "Black Olives")
    )
    toppings = models.CharField(max_length=16, choices=TOPPINGS)


# class Pizza(models.Model):
#     SIZE = (("S", "Small"), ("L", "Large"))
#     price = models.FloatField(max_length=4)
#     size = models.CharField(max_length=8, choices=SIZE)
class Pizza(models.Model):
    name = models.TextField(max_length=32, default='pizza')
    small_price = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)
    large_price = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)

    def __str__(self):
        return self.name
    

class RegularPizza(models.Model):
    pizza = models.OneToOneField(
        Pizza,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


class SicilianPizza(models.Model):
    pizza = models.OneToOneField(
        Pizza,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name


class Sub(models.Model):
    name = models.TextField(max_length=32)
    small_price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Pasta(models.Model):
    name = models.TextField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Salad(models.Model):
    name = models.TextField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class DinnerPlatters(models.Model):
    name = models.TextField(max_length=32)
    small_price = models.DecimalField(max_digits=4, decimal_places=2)
    large_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name