from django.urls import path
from register_app import views

urlpatterns = [
    path('', views.register, name='register'),
    
]