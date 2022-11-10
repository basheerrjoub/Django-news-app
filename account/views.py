from django.shortcuts import render
from account.forms import LoginForm
from .forms import LoginForm, UserRegister
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse

# Create your views here.


class LogUser(LoginView):
    template_name = "account/login.html"


class LogoutViewUser(LogoutView):
    template_name = "home.html"


def register(request):
    if request.method == "POST":
        user = UserRegister(request.POST)
        if user.is_valid():
            new_user = user.save(commit=False)
            new_user.set_password(user.cleaned_data["password"])
            new_user.save()
            return render(request, "account/register_done.html", {"user": new_user})
    else:
        user = UserRegister()
    return render(request, "account/register.html", {"user": user})
