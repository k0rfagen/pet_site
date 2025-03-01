from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/%Y%m%d', blank=True)
    description = models.TextField(default='')
    def __str__(self):
        return f'{self.name}, price: {self.price}, description: {self.description}'

class CartItem(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart_id = models.CharField(max_length=100)
    def get_cost(self):
        return self.item.price * self.quantity
    def __str__(self):
        return f'{self.quantity} x {self.item} in {self.cart_id}'
