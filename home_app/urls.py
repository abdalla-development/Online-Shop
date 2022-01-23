from django.urls import path
from home_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
]