from django import forms
from .models import *

class SearchForm(forms.Form):
    search_body = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Поиск...',
        'class': 'search-text',
         }))
