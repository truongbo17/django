from django.shortcuts import render
from .forms import userFromContact
from django.http import HttpResponse


# Create your views here.
def index(request):
    contact_form = userFromContact
    return render(request, 'contact/index.html', {'contact_form': contact_form})


def getContact(request):
    if request.method == "POST":
        contact_form = userFromContact(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponse("Success send contact")
    else:
        return HttpResponse("Fail send contact")
