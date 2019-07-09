from django.db import models
from shop.models import Product
from django.contrib.auth import get_user_model


STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)

user_model = get_user_model()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def get_full_price(self):
        return  self.product.price * self.amount

    def __str__(self):
        return f'{self.product.title} - {self.amount} '


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)


    def __str__(self):
        return f'Cart id: {self.id}'


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=120, default='SMTHN', unique=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')

    def __str__(self):
        return self.order_id
