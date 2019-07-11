from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from carts.models import Cart
from carts.models import CartItem
from shop.models import Product


def update_cart(request, product_id):
    request.session.set_expiry(120000)
    print(request.session.__dict__)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = get_object_or_404(Cart, id=the_id)
    product = get_object_or_404(Product, id=product_id)
    product.amount = 1
    product.save()
    cart_item, created = CartItem.objects.get_or_create(product=product)

    if not cart_item in cart.items.all():
        cart_item.amount = 1
        cart_item.save()
        cart.items.add(cart_item)
    else:
        cart.items.remove(cart_item)

    new_total = 0.00
    for item in cart.items.all():
        new_total += float(item.get_full_price())
    request.session['items_total'] = cart.items.count()
    if not request.session['items_total']:
        return redirect('to_home_url')
    cart.total = new_total
    cart.save()
    return redirect('view_cart_url')
