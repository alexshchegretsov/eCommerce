from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import SignUpForm


def to_home(request): pass


def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'accounts/sign_up.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect('to_home_url')
        return redirect('sign_up_url')
    return HttpResponse('INVALID REQUEST METHOD')
