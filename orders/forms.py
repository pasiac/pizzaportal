from django import forms

from .models import CartItem


# trzeba ustawić ifa dla kategorii i jak
# ma tylko small price to zeby nie bylo wyboru wielkosci
class ItemDetailsForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ["size", "quantity", "topping"]
