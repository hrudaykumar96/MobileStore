"""mobilestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apple.views import apple
from home.views import home
from login.views import signin
from logout.views import signout
from mi.views import mi
from oneplus.views import oneplus
from oppo.views import oppo
from realme.views import realme
from register.views import signup
from samsung.views import samsung
from vivo.views import vivo
from reset_password.views import password_reset

urlpatterns = [
    path("admin/", admin.site.urls),
    path("apple/",apple, name="apple"),
    path("home/",home,name="home"),
    path("",signin,name="login"),
    path("logout/",signout,name="logout"),
    path("mi/",mi,name="mi"),
    path("oneplus/",oneplus,name="oneplus"),
    path("oppo/",oppo,name="oppo"),
    path("realme/",realme,name="realme"),
    path("register/",signup,name="register"),
    path("samsung/",samsung,name="samsung"),
    path("vivo/",vivo,name="vivo"),
    path("password_reset/",password_reset,name="reset"),
]

