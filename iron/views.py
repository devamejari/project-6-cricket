from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def tarak(request):
    return HttpResponse('<h1> this is tarak</h1>')