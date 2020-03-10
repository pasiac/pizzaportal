from django.test import TestCase

from orders.factories import *
from orders.forms import ItemDetailsForm

STATUS_OK = 200


class OrdersTest(TestCase):
    def setUp(self) -> None:
        self.topping = ToppingFactory()
        self.item = ItemFactory(name="test")
        self.cart_item = CartItemFactory()
        # self.cart = UserCartFactory()

    def test_index_page_returns_status_code_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, STATUS_OK)

    def test_menu_page_returns_menu(self):
        response = self.client.get("/menu")
        self.assertContains(response, "test")

    # def test_cart_returns_cart_items(self):
    #     response = self.client.get("/cart")
    #     self.assertContains(response, self.cart.items)

    def test_item_details_returns_valid_form(self):
        response = self.client.get("/details/" + self.item.slug)
        self.assertEqual(response.status_code, STATUS_OK)
        self.assertContains(response, self.topping)
        self.assertContains(response, "Quantity")
        self.assertContains(response, "Size")

    # Nie wiem czemu to nie dziala
    # def test_ItemDetailsForm(self):
    #     form_data = {"size": "Small", "quantity": 1, "topping": self.topping}
    #     form = ItemDetailsForm(data=form_data)
    #     self.assertTrue(form.is_valid())
