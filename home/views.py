from django.http import HttpResponse
from django.shortcuts import render
from .models import Upload
from .forms import UploadFileForm


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def upload(request):
    upload_form = UploadFileForm
    return render(request, 'home/upload.html', {
        'upload_form': upload_form
    })


def saveFile(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("Save file success")
    else:
        return HttpResponse("Save file fail")
