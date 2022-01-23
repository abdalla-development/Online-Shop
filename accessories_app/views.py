from django.shortcuts import render, redirect
from django.http import HttpResponse
from accessories_app.models import Accessories
from accessories_app.form import AccessoriesForm
from django.contrib import messages
from cart_app.models import Cart
from django.core.paginator import Paginator
from django.contrib.auth.models import User, auth

# Create your views here.
def accessories(request):
    # Data to be shown

    # Get the user IP
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
   
    # Get the cart item related to the user
    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)

    # Get the number of items in the cart related to the user
    items_in_cart= len(cart_all)

    # Using Pagination
    accessories_all = Accessories.objects.all()
    paginator = Paginator(accessories_all, 4)
    page = request.GET.get("page")
    accessories_all = paginator.get_page(page)


    content = {
        'accessories_outfit': accessories_all
    }
    if request.method == "GET":
        return render(request, 'accessories.html', {"accessories_all": accessories_all, "items_in_cart": items_in_cart, 'ip': ip,})
    
def accessory(request, item_id):
    # show the selected item
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))

    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)

    items_in_cart= len(cart_all)
    item_to_show = Accessories.objects.get(pk=item_id)

    if request.method == "GET":
        return render(request, 'accessories_item.html', {"item": item_to_show, "items_in_cart": items_in_cart, 'ip': ip,})
    else:
        form = AccessoriesForm(request.POST or None)
        messages.success(request, 'Item successfully added to the Cart.')
        if form.is_valid():
            form.save()
            print("form is valid")
        else:
            print("form is not valid")
        return redirect('accessories')


# Getting the IP function
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip