from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('boys/', include('boys_app.urls')),
    path('girls/', include('girls_app.urls')),
    path('accessories/', include('accessories_app.urls')),
    path('cart/', include('cart_app.urls')),
    path('checkout/', include('checkout_app.urls')),
    path('login/', include('login_app.urls')),
    path('register/', include('register_app.urls')),
]
