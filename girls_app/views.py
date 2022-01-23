from django.shortcuts import render, redirect
from django.http import HttpResponse
from girls_app.models import Girls
from girls_app.form import GirlsForm
from django.contrib import messages
from django.core.paginator import Paginator
from cart_app.models import Cart
from django.contrib.auth.models import User, auth

# Create your views here.
def girls(request):
    # Data to be shown
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)
    items_in_cart= len(cart_all)
    girls_all = Girls.objects.all()
    paginator = Paginator(girls_all, 4)
    page = request.GET.get("page")
    girls_all = paginator.get_page(page)
    content = {
        'gilrs_outfit': girls_all
    }

    return render(request, 'girls.html', {"girls_all": girls_all, "items_in_cart": items_in_cart, 'ip': ip,})

def girl(request, item_id):
    # show the selected item
    ip = get_client_ip(request)
    ip = int(ip.replace(".", ""))
    if request.user.is_authenticated:
        cart_all = Cart.objects.filter(user_id= request.user)
    else:
        cart_all = Cart.objects.filter(user_id= ip)
    items_in_cart= len(cart_all)
    item_to_show = Girls.objects.get(pk=item_id)
    if request.method == "GET":
        return render(request, 'girls_item.html', {"item": item_to_show, "items_in_cart": items_in_cart, 'ip': ip,})
    else:
         form = GirlsForm(request.POST or None)
        # print(item_to_show.image)
        # print(request.POST['colors'])
         image = item_to_show.image
         item_name = item_to_show.item_name
         price = item_to_show.price
         amount = request.POST['amount']
         colors = request.POST['colors']
         sizes = request.POST['sizes']
         category = item_to_show.category
        # quantity 
        # total
         messages.success(request, 'Item successfully added to the Cart.')
         if form.is_valid():
            form.save()
         return redirect('girls')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip