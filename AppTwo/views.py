from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    my_dict = {'django_reinhardt': "This is Django on first_app/index.html!"}
    return render(request, 'first_app/index.html', context=my_dict)

def profile(request):
    return render(request, 'first_app/profile.html')

def help(request):
    return render(request, 'help.html')