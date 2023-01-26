from django.shortcuts import render
from .forms import registerForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse


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
