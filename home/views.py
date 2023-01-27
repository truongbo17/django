from django.http import HttpResponse
from django.shortcuts import render
from .models import Upload, UploadMultiple
from .forms import UploadFileForm, UploadMultiFileForm
from .models import Category
from django.views.generic.edit import FormView


# Create your views here.
def index(request):
    list_category = Category.objects.all()
    return render(request, 'home/index.html', {'list_category': list_category})


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


class FileFieldFormView(FormView):
    def get(self, request):
        multiple_file = UploadMultiFileForm
        return render(request, 'home/upload_multiple.html', {
            'multiple_file': multiple_file
        })

    def post(self, request):
        multiple_file = UploadMultiFileForm
        multiple_file = self.get_form(multiple_file)
        files = request.FILES.getlist('images')
        if multiple_file.is_valid():
            for f in files:
                instance = UploadMultiple(images=f)
                instance.save()
        return HttpResponse("Save file success")
