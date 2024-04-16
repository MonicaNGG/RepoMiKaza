from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import CustomSignupForm

def register(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirigir a home si el usuario ya ha iniciado sesión
    
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'app_account/register.html', {'form': form})



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirigir a home si el usuario ya ha iniciado sesión
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Asegúrate de tener una vista 'home' definida
            else:
                form.add_error(None, 'Username or Password is not valid')
    else:
        form = AuthenticationForm()
    return render(request, 'app_account/login.html', {'form': form})
