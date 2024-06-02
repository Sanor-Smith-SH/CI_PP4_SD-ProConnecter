"""servicetisement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('available-services/', views.available_services, name='available_services'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('register/', views.register, name='register'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('operations/', views.operations, name='operations'),
    path('add-service/', views.add_service, name='add_service'),
    path('update-service/<int:service_id>/', views.update_service, name='update_service'),
    path('remove-service/<int:service_id>/', views.remove_service, name='remove_service'),
]