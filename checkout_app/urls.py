from django.urls import path
from checkout_app import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('charge', views.charge, name='charge'),
]