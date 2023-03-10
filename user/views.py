from django.shortcuts import render, redirect
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Register(View):
    @staticmethod
    def get(request):
        register_form = registerForm
        return render(request, 'user/register.html', {'register_form': register_form})

    @staticmethod
    def post(request):
        if request.method == "POST":
            register_form = registerForm(request.POST)
            if register_form.is_valid():
                user = User.objects.create_user(
                    username=register_form.cleaned_data['user_name'],
                    email=register_form.cleaned_data['email'],
                    password=register_form.cleaned_data['password'],
                )
                user.save()
                return HttpResponse("Save user success")
        else:
            return HttpResponse("Save user fail")


class Login(View):
    @staticmethod
    def get(request):
        login_form = loginForm
        return render(request, 'user/login.html', {'login_form': login_form})

    @staticmethod
    def post(request):
        if request.method == "POST":
            login_form = loginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data['user_name'],
                    password=login_form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('user:privatePage')
                else:
                    return HttpResponse("Password or username in valid")
        else:
            return HttpResponse("Login user fail")


def logoutUser(request):
    logout(request)
    return redirect('user:login')


@login_required(login_url='/user/login')
def privatePage(request):
    return render(request, "user/private.html")


class PrivatePage(LoginRequiredMixin, View):
    login_url = '/user/login'

    @staticmethod
    def get(request):
        return render(request, "user/private.html")
