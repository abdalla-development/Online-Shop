from django.urls import path
from login_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('login', auth_views.LoginView.as_view(templates_name='login.html'), name='login'), 
    #  path('logout', auth_views.LogoutView.as_view(templates_name='logout.html'), name='logout'), 
]