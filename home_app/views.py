from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from cart_app.models import Cart
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)
    items_in_cart= len(cart_all)
    return render(request, 'index.html', {"items_in_cart": items_in_cart, 'ip': ip,})

def contact(request):
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
    if request.method == "GET":
        if request.user.is_authenticated:
            cart_all = Cart.objects.filter(user_id= request.user)
        else:
            cart_all = Cart.objects.filter(user_id= ip)
        items_in_cart= len(cart_all)
        return render(request, 'contact.html', {"items_in_cart": items_in_cart, 'ip': ip,})
    else:
        pass

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip