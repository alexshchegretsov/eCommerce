from django.shortcuts import render
from django.utils import timezone
from shop.models import Category


def to_home_view(request):
    current_hour = timezone.now().hour + 3
    request.session['is_work_time'] = 8 <= current_hour < 22
    categorys = Category.objects.all()
    context = {'categorys': categorys}
    return render(request, 'shop/to_home.html', context)
