from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello1(request):
    return HttpResponse("Hello, world")

def root(request):
    return HttpResponse("<a href='hello'>to Hello</a>")