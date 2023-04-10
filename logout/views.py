from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def signout(request):
    logout(request)
    messages.success(request, "You are logged out successfully")
    return redirect('login')