from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available-services/', views.available_services, name='available_services'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('register/', views.register, name='register'),
    path('operations/', views.operations, name='operations'),
    path('add-service/', views.add_service, name='add_service'),
    path('update-service/', views.update_service, name='update_service'),
    path('remove-service/', views.remove_service, name='remove_service'),
    
]
