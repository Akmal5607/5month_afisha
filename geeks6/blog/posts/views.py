from django.shortcuts import HttpResponse, redirect


# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, its my first View! :)')


def redict_to_youtube_view(request):
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')


def google(request):
    if request.method == 'GET':
        return redirect('https://www.google.com/')


def git(request):
    if request.method == 'GET':
        return redirect('https://github.com/')
