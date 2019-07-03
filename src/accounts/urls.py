from django.urls import path
from django.contrib.auth import views as auth_views

from .views import to_home, sign_up

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout_url'),
    path('home/', to_home, name='home_url'),
    path('signup/', sign_up, name='sign_up_url'),
]
