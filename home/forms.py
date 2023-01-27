from django import forms
from .models import Upload


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title', 'image', 'body']


class UploadMultiFileForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
