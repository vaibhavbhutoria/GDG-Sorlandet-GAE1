from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return HttpResponse("Hello world")


