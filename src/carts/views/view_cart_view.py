from django.shortcuts import render
from carts.models import Cart


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