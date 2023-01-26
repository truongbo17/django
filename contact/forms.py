from django import forms


class contactForm(forms.Form):
    user_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)
