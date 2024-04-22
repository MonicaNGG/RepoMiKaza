from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from .forms import CustomSignupForm
from .models import User

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # El usuario no se activa hasta que verifique su correo
            user.save()
            
            # Crear enlace de activación y enviar por correo
            activation_link = request.build_absolute_uri(
                reverse('activate_account', kwargs={'token': user.activation_token}))
            send_mail(
                'Por favor activa tu cuenta',
                f'Activa tu cuenta a través del siguiente enlace: {activation_link}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
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


def activate_account(request, token):
    User = get_user_model()
    try:
        user = User.objects.get(activation_token=token, is_active=False)
        user.is_active = True
        user.activation_token = None  # Limpiar el token después de la activación
        user.save()
        login(request, user)  # Opcional: iniciar sesión automáticamente después de activar
        return redirect('home')
    except User.DoesNotExist:
        return redirect('home')
        #return render(request, 'app_account/activation_invalid.html')
