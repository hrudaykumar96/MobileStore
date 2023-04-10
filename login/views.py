from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = User.objects.filter(email=email).first()
            if user_obj is None:
                messages.info(request,"Email Id does not registered")
                return redirect("register")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,"Incorrect Email Id or Password")
                return redirect('login')
        return render(request, "login.html")
    else:
        return redirect ("home")
