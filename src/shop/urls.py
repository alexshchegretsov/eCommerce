from django.urls import path
from .views import to_home_view
from .views import show_category
from .views import product_detail

urlpatterns = [
    path('', to_home_view, name='to_home_url'),
    path('category/<int:category_id>/', show_category, name='show_category_url'),
    path('product/<int:product_id>/', product_detail, name='product_detail_url'),
]
