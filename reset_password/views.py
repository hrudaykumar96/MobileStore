from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def password_reset(request):
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("pass1")
        confirm_password = request.POST.get("pass2")
        if new_password == confirm_password:
            c = User.objects.filter(email=email).first()
            if c is None:
                messages.info(request,"Email Id not registered")
                return redirect("register")
            c.set_password(new_password)
            c.save()
            messages.success(request, "Password Changed Successfully")
            return redirect ("login")
    return render(request,"reset.html")
