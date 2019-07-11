from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from accounts.forms import SignUpForm
from carts.models import Cart


def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/sign_up.html', {'form': form})
    elif request.method == 'POST':
        try:
            the_id = request.session['cart_id']
            cart = Cart.objects.get(id=the_id)
            cart.items.clear()
        except:
            pass
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            login(request, user)
            return redirect('to_home_url')
        return redirect('sign_up_url')
    return HttpResponse('INVALID REQUEST METHOD')