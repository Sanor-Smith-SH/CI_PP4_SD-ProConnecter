from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Service
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegisterForm, CustomUserCreationForm

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
            return redirect('operations')
        else:
            username = request.POST.get('username')
            user = authenticate(username=username, password=request.POST.get('password'))
            if user is None:
                messages.error(request, 'User does not exist. Do you want to register?')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('operations')
        else:
            if 'email' in form.errors:
                messages.error(request, form.errors['email'][0])
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('home')

def operations(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    return render(request, 'operations.html')

def add_service(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        occupation = request.POST.get('occupation')
        contact_info = request.POST.get('contact_info')
        featured_image = request.FILES.get('featured_image')

        service = Service.objects.create(
            ads_auther=request.user,
            title=title,
            description=description,
            occupation=occupation,
            contact_info=contact_info,
            featured_image=featured_image
        )
        service.save()
        messages.success(request, 'Service added successfully')
        return redirect('operations')
    return HttpResponse(status=405)

def update_service(request, service_id):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    service = Service.objects.get(id=service_id, ads_auther=request.user)
    if request.method == 'POST':
        service.title = request.POST.get('title')
        service.description = request.POST.get('description')
        service.occupation = request.POST.get('occupation')
        service.contact_info = request.POST.get('contact_info')
        if request.FILES.get('featured_image'):
            service.featured_image = request.FILES.get('featured_image')
        service.save()
        messages.success(request, 'Service updated successfully')
        return redirect('operations')
    return HttpResponse(status=405)

def remove_service(request, service_id):
    if not request.user.is_authenticated:
        return redirect('sign_in')
    service = Service.objects.get(id=service_id, ads_auther=request.user)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service removed successfully')
        return redirect('operations')
    return HttpResponse(status=405)
