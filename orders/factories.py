import factory
import factory.fuzzy
from django.contrib.auth.models import User

from orders.models import *


class ToppingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topping
        django_get_or_create = ("name", "price")

    name = factory.fuzzy.FuzzyText(length=10)
    price = factory.fuzzy.FuzzyFloat(low=0.5, high=3)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name = factory.fuzzy.FuzzyText(length=20)


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item
        # django_get_or_create = ("name", "small_price", "large_price", "slug", "category")

    name = factory.fuzzy.FuzzyText(length=10)
    small_price = factory.fuzzy.FuzzyFloat(low=1, high=20)
    large_price = factory.fuzzy.FuzzyFloat(low=1, high=20)
    slug = factory.fuzzy.FuzzyText(length=6)
    category = factory.SubFactory(CategoryFactory)


class CartItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CartItem
        # django_get_or_create = ("item", "quantity", "size", "topping")

    item = factory.SubFactory(ItemFactory)
    quantity = factory.fuzzy.FuzzyInteger(low=1, high=10)
    size = factory.Iterator(["Small", "Large"])
    topping = factory.SubFactory(ToppingFactory)

    @factory.post_generation
    def topping(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for topping in extracted:
                self.topping.add(topping)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.fuzzy.FuzzyText(length=10)
    password = factory.fuzzy.FuzzyText(length=12)


class UserCartFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserCart
        django_get_or_create = (
            "user",
            "value",
        )

    value = factory.fuzzy.FuzzyFloat(low=1, high=100)
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def items(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for item in extracted:
                self.items.add(item)
