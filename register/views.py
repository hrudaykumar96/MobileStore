from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username = email).first():
            messages.error(request, "Email Id already registered")
            return redirect('login')
        c = User.objects.create_user(first_name=first_name,last_name=last_name,username=email, email=email,password=password)
        c.save()
        messages.success(request,"Account Created Successfully you can login now")
        return redirect("login")
    return render(request, "register.html")