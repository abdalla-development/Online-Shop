from django.shortcuts import render, redirect
from django.http import HttpResponse
import stripe
from django.conf import settings
from django.urls import reverse
from cart_app.models import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

# Create your views here.
@login_required
def checkout(request):
    # user = auth.is_authenticate()
        
    total = 0
    cart_all = Cart.objects.filter(user_id= request.user)
    for obj in cart_all:
        total += obj.price
        if obj.user_id is None:
            obj.user_id = request.user
            obj.save()
    items_in_cart= len(cart_all)
    print(request.user)
    # stripe.api_key = settings.STRIPE_PRIVATE_KEY

    # session = stripe.checkout.Session.create(
    # # success_url= request.build_absolute_url( reverse('home')) + '?session_id{ CHECKOUT_SESSION_ID }',
    # # cancel_url= request.build_absolute_url( reverse('home')),
    # success_url="https://example.com/success",
    # cancel_url= "https://example.com/cancel",
    # payment_method_types=["card"],
    # line_items=[
    #     {
    #     "price": "price_1Jb6rVAaHGNBSg8S8V5LEvkU",
    #     "quantity": 1,
    #     },
    # ],
    # mode="payment",
    # )

    context = {
        # 'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'total': total,
        "items_in_cart": items_in_cart,
    }
    return render(request, 'checkout.html', {'total': total, 'cart_all': cart_all, "items_in_cart": items_in_cart,})

def charge(request):
    if request.method == "GET":
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        return render (request, 'charge.html', {'key': stripe.api_key})
    else:
        charges = stripe.Charge.create(
            amount = 500,
            currency = 'usd',
            description = 'Payment Gateaway',
            source = request.POST['stripeToken']
        )
        return render (request, 'charge.html', {})
    