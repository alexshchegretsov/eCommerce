from django.db import models
from shop.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def get_full_price(self):
        return self.product.price * self.amount

    def __str__(self):
        return f'{self.product.title}'


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Cart id: {self.id}'
