from django import forms

from .models import OrderItem


class ItemDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            'size',
            'addon1',
            'addon2',
            'addon3'
        ]