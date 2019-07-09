from django.contrib import admin
from .models import Cart
from .models import Order

admin.site.register(Cart)
admin.site.register(Order)