from django import forms
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm, PasswordChangeForm

from .models import *


class SearchForm(forms.Form):
    search_body = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Поиск...",
                "class": "search-text",
                "oninput": "searchTips()",
            }
        ),
    )


class RegistrationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = BaseUserCreationForm.Meta.fields + ('email', )

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'image')

