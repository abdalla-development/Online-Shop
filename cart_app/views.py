from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from cart_app.models import Cart
# from cart_app.form import CartForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth

# Create your views here.
def cart(request):
    # Data to be shown
    total = 0
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)
    items_in_cart= len(cart_all)
    paginator = Paginator(cart_all, 4)
    page = request.GET.get("page")
    cart_all = paginator.get_page(page)
    for obj in cart_all:
        total += obj.price
    content = {
        'boys_outfit': cart_all
    }
    if request.method == "GET":
        return render(request, 'cart.html', {"cart_all": cart_all, "items_in_cart": items_in_cart, "total": total})

def delete(request, item_id):
    cart_item = Cart.objects.get(pk=item_id)
    # if cart_item.user_id == request.user:
    cart_item.delete()
    # else:
        # messages.error("Access restricted, You are not allowed")
    return redirect('cart')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip