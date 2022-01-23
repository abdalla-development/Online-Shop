from django.urls import path
from boys_app import views

urlpatterns = [
    path('', views.boys, name='boys'),
    path('<item_id>', views.boy, name='boy'),
    
]