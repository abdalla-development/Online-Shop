from django.urls import path
from girls_app import views

urlpatterns = [
    path('', views.girls, name='girls'),
    path('<item_id>', views.girl, name='girl'),
    
]