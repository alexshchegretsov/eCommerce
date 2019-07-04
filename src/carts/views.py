from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
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

    if not product in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
        product.amount = 1
        product.save()

    new_total = 0.00
    for item in cart.products.all():
        new_total += float(item.get_total)
    request.session['items_total'] = cart.products.count()
    cart.total = new_total
    cart.save()
    return redirect('view_cart_url')


def increase_amount(request, product_id):
    cart = get_object_or_404(Cart, id=request.session['cart_id'])
    product = get_object_or_404(Product, id=product_id)
    product.amount += 1
    product.save()
    cart.total += product.price
    cart.save()
    return redirect('view_cart_url')


def decrease_amount(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.amount == 1:
        return redirect('view_cart_url')
    product.amount -= 1
    product.save()
    cart = get_object_or_404(Cart, id=request.session['cart_id'])
    cart.total -= product.price
    cart.save()
    return redirect('view_cart_url')
