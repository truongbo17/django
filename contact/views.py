from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm
from .models import ContactFormModel
from django.views import View


# Create your views here.
class Contact(View):

    @staticmethod
    def get(request):
        contact_form = contactForm
        return render(request, 'contact/index.html', {'contact_form': contact_form})

    @staticmethod
    def post(request):
        if request.method == "POST":
            contact_form = contactForm(request.POST)
            if contact_form.is_valid():
                saveContactModel = ContactFormModel(
                    user_name=contact_form.cleaned_data['user_name'],
                    email=contact_form.cleaned_data['email'],
                    body=contact_form.cleaned_data['body'],
                )
                saveContactModel.save()
                return HttpResponse("Save success")
        else:
            return HttpResponse("Save fail")
