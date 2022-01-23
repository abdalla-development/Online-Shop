from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password= password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Wrong Username or Password")
            return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('home')
