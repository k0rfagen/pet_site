from django import forms
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm

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
