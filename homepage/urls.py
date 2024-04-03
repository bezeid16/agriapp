# homepage/urls.py

from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('register/', register, name='register')

]

