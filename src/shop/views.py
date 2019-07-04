from django.shortcuts import render
from .models import Category, Product
from carts.models import Cart

def to_home_view(request):
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'shop/to_home.html', context)


def show_category(request, category_id):
    products = Product.objects.filter(category__id=category_id)
    context = {'products': products, 'category': Category.objects.get(id=category_id)}
    return render(request, 'shop/show_category.html', context)


def product_detail(request, product_id):
    print(request.user)
    print(request.COOKIES)
    print(request.session.__dict__)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    product = Product.objects.get(id=product_id)
    context = {'product': product,'cart': cart}
    return render(request, 'shop/product_detail.html', context)
