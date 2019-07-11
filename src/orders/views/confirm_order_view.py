from django.shortcuts import redirect
from django.shortcuts import render
from carts.models import Cart
from orders.models import Order
from orders.models import OrderItem
from shop.models import Product
from django.contrib.auth import get_user


def confirm_order(request):
    if request.method == 'POST':
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
                total=cart.total,
            )
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
                total=cart.total,
            )
        order.save()

        for item in cart.items.all():
            product = Product.objects.get(id=item.product.id)
            current_order_item = OrderItem.objects.create(product=product, amount=item.amount)
            current_order_item.save()
            order.order_items.add(current_order_item)
        cart.items.clear()
        del request.session['cart_id']
        request.session['items_total'] = 0
        return render(request, 'orders/successfully_created.html', context={'order': order})
    return redirect('to_home_url')
