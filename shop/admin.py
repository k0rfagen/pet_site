from django.contrib import admin

from shop.models import Items


# Register your models here.
@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    display = ("name", "price")
