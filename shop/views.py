from django.shortcuts import render
from shop.models import Items
from django.views.generic.base import View


# Create your views here.
class ItemView(View):
    def get(self, request):
        items = Items.objects.all()
        context = {
            'items': items
        }
        return render(request, 'index.html', context)