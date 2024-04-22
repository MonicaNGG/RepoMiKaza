from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Username',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Email Address',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field', 
        'placeholder': 'First Name',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Last Name',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Phone Number',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Password',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Confirm Password',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field', 
        'placeholder': 'Username or Email Address',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-field',
        'placeholder': 'Enter your Password',
        'style': 'width: 100%; padding: 10px; border: none; border-bottom: 2px solid gray; margin-bottom: 20px;'
    }))
