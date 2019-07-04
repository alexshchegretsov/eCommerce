from django.db import models
from shop.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return f'Cart id: {self.id}'