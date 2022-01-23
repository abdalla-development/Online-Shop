from django.shortcuts import render, redirect
from django.http import HttpResponse
from register_app.form import RegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {})
    elif request.method == "POST":
        form = RegisterForm(request.POST or None)
        #print(request.POST['first_name'])
        if form.is_valid():
            form.save()
            messages.success(request, 'New User added.') 
            return redirect('login')  #
        else:
            # print("form no valid")
            for msg in form.error_messages:
                messages.error(request, 'User Not added.')
                print(msg)  
            return redirect('register')