from django import forms


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    password2 = forms.CharField(widget=forms.PasswordInput())
    password3 = forms.CharField(widget=forms.PasswordInput())
