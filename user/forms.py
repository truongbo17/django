from django import forms


class registerForm(forms.Form):
    user_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class loginForm(forms.Form):
    user_name = forms.CharField(max_length=120)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
