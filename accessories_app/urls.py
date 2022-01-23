from django.urls import path
from accessories_app import views

urlpatterns = [
    path('', views.accessories, name='accessories'),
    path('<item_id>', views.accessory, name='accessory'),
    # path('accessory/<item_id>', views.add_accessory, name='add_accessory'),
    
]