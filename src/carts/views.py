from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Cart
from .models import CartItem
from shop.models import Product



def view_cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)
    context = {'cart': cart}

    return render(request, 'carts/view_cart.html', context)


# Unittest area

def update_cart(request, product_id):
    request.session.set_expiry(120000)
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
        new_total += float(item.product.get_total)
    request.session['items_total'] = cart.items.count()
    cart.total = new_total
    cart.save()
    return redirect('view_cart_url')


def increase_amount(request, cart_item_id):
    cart = get_object_or_404(Cart, id=request.session['cart_id'])
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.amount += 1
    cart_item.save()
    cart.total += cart_item.product.price
    cart.save()
    return redirect('view_cart_url')


def decrease_amount(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item.amount == 1:
        return redirect('view_cart_url')
    cart_item.amount -= 1
    cart_item.save()
    cart = get_object_or_404(Cart, id=request.session['cart_id'])
    cart.total -= cart_item.product.price
    cart.save()
    return redirect('view_cart_url')