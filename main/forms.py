from django import forms
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(forms.ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)