from django.db import models
from carts.models import Cart
from django.contrib.auth import get_user_model

user_model = get_user_model()

STATUS_CHOICES = (
    ('Started', 'Started'),
    ('Abandoned', 'Abandoned'),
    ('Finished', 'Finished'),
)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=120)
    delivery_time = models.DateTimeField()
    order_id = models.CharField(max_length=120, default='SMTHN', unique=True)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')

    def __str__(self):
        return self.order_id
