from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from users.forms import AuthForm

from user.forms import RegisterForm


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm
        }

        return render(request, 'users/auth.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = AuthForm(data=data)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

            if user:
                login(request, user)
                return redirect('/posts/')
            else:
                form.add_error('username','try again :(')

         return render(request, 'users/register.html', context={
                    'form': form
                })


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data=data)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )

            login(request, user)
            return redirect('/posts/')
        else:
            form.add_error('password1', 'password1 != password2')

        return render(request, 'users/register.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('/posts/')

 