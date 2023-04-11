from django.shortcuts import render, redirect
from GamifApp.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to the home view after a successful login
    else:
        form = AuthenticationForm()
    return render(request, 'GamifApp/login.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to the login view after a successful registration
    else:
        form = RegistrationForm()
    return render(request, 'GamifApp/signup.html', {'form': form})
def home(request):
    return render(request, 'GamifApp/home.html')
