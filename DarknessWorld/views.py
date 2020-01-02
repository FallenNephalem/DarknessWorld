from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('Welcome to Darkness World')

def content(request):
    return render(request, 'DarknessWorld/hello.html')

def inventory(request):
    return render(request, 'DarknessWorld/hello.html', context={'ShowInventory': True})
