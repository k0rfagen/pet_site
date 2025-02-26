from .models import Items
from django.forms import ModelForm, forms, TextInput


class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'price', 'quantity', 'id']
        widgets = {
            'name': forms.TextInput(attrs={
                'search': 'search',
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'search',
                'id': 'item',
            }),
        }