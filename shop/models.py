from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/%Y%m%d', blank=True)
    def __str__(self):
        return f'{self.name}, price: {self.price}'
