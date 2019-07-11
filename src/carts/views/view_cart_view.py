from django.shortcuts import render
from django.shortcuts import redirect
from carts.models import Cart


def view_cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        return redirect('to_home_url')
    cart = Cart.objects.get(id=the_id)
    context = {'cart': cart}
    return render(request, 'carts/view_cart.html', context)