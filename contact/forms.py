from django import forms
from .models import ContactFormModel


class userFromContact(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['user_name', 'email', 'body']
