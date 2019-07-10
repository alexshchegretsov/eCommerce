from django.db import models
from carts.models import Cart
from carts.models import CartItem
from shop.models import Product
from django.contrib.auth import get_user_model

user_model = get_user_model()

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} - {self.amount}'



class Order(models.Model):
    order_items = models.ManyToManyField(OrderItem)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    phone = models.CharField(max_length=254)
    delivery_address = models.CharField(max_length=120, default='')
    delivery_time = models.CharField(max_length=120, default='00:00:00')
    order_id = models.CharField(max_length=120, default='SMTHN', unique=True)
    comment = models.TextField(max_length=300, blank=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')

    def __str__(self):
        return self.order_id
