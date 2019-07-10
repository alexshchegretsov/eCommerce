from django.urls import path
from .views import confirm_order


urlpatterns = [
    path('', confirm_order, name='confirm_order_url' ),
]