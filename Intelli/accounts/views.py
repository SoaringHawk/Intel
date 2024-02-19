

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created! You are now logged in.')
            return redirect('home')  # Adjust the redirect to where you want users to go to after registration
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/registration/register.html', {'form': form})


def home(request):
    return render(request, 'accounts/index.html')