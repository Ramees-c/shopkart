from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import Customer
from django.contrib import messages

# Create your views here.
def show_account(request):
    contex = {}
    if request.method == 'POST' and 'register' in request.POST :
        contex['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # create user account 
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            # create customer account
            customer = Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_message = "User Created"
            messages.success(request, success_message)
        except Exception as e:
            error_message = "Duplicate username or invalid inputs"
            messages.error(request, error_message)
    if request.method == 'POST' and 'login' in request.POST :
        contex['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user :
            login(request, user)
            return redirect('home')
        else :
            messages.error(request, 'invalid user credintials')
    return render(request, 'account.html', contex)

def signout(request):
    logout(request)
    return redirect('account')

