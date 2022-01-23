from django import forms
from django.forms import fields
from cart_app.models import Cart


class BoysForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['item_name', 'image', 'price', 'amount', 'colors', 'sizes', 'category', 'user_id']