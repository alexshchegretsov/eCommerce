from django.urls import path
from .views import view_cart
from .views import update_cart
from .views import increase_amount
from .views import decrease_amount

urlpatterns = [
    path('', view_cart, name='view_cart_url'),
    path('<int:product_id>/', update_cart, name='update_cart_url'),
    path('increase/<int:cart_item_id>/', increase_amount, name='increase_url'),
    path('decrease/<int:cart_item_id>/', decrease_amount, name='decrease_url'),
]
