from django.shortcuts import render
from shop.models import Product
from shop.models import Category


def show_category(request, category_id):
    products = Product.objects.filter(category__id=category_id)
    context = {'products': products, 'category': Category.objects.get(id=category_id)}
    return render(request, 'shop/show_category.html', context)
