from django.shortcuts import render
from carts.models import Cart
from shop.models import Product


def product_detail(request, product_id):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    product = Product.objects.get(id=product_id)
    context = {'product': product, 'cart': cart}
    return render(request, 'shop/product_detail.html', context)
