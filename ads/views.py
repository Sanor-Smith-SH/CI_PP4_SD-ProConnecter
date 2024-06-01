from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Service 

def home(request):
    return render(request, 'home.html')

def available_services(request):
    occupation = request.GET.get('occupation')
    if occupation:
        services = Service.objects.filter(occupation=occupation)
    else:
        services = Service.objects.all()
    occupations = Service.objects.values_list('occupation', flat=True).distinct()
    return render(request, 'available_services.html', {'services': services, 'occupations': occupations})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            # Check if the error is due to non-existent user
            username = request.POST.get('username')
            user = authenticate(username=username, password=request.POST.get('password'))
            if user is None:
                messages.error(request, 'User does not exist. Do you want to register?')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
