from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from carts.models import CartItem
from carts.models import Cart


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
