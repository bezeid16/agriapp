# homepage/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm



def home(request):
    return render(request, 'homepage/home.html')



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
