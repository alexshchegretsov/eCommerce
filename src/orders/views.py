from django.shortcuts import redirect
from carts.models import Cart
from .models import Order
from .models import OrderItem
from shop.models import Product
from django.contrib.auth import get_user

def confirm_order(request):
    user = get_user(request)
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)
    try:
        last_order = Order.objects.last()
        order_id = last_order.id
    except:
        order_id = 0
    if request.user.is_authenticated:
        order = Order.objects.create(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
            delivery_address=request.POST.get('delivery_address'),
            delivery_time=request.POST.get('delivery_time'),
            order_id=order_id + 1,
            comment=request.POST.get('comment'),
            cart=cart,
        )
        order.save()
        # del request.session['items_total']
        print(cart.items.all())
    else:
        order = Order.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            delivery_address=request.POST.get('delivery_address'),
            delivery_time=request.POST.get('delivery_time'),
            order_id=order_id + 1,
            comment=request.POST.get('comment'),
            cart=cart,
        )
        order.save()
    for item in cart.items.all():
        product = Product.objects.get(id=item.product.id)
        product_amount = item.amount
        current_order_item = OrderItem.objects.create(product=product, amount=product_amount)
        current_order_item.save()
        order.order_items.add(current_order_item)
    cart.items.clear()
    request.session['items_total'] = cart.items.count()
    return redirect('to_home_url')