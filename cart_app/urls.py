from django.urls import path
from cart_app import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('<item_id>', views.delete, name='delete'),
    
]