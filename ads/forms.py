from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Service

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['occupation', 'description', 'featured_image']

class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['occupation', 'description', 'featured_image']
        
class ServiceDeleteForm(forms.Form):
    service_id = forms.IntegerField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']