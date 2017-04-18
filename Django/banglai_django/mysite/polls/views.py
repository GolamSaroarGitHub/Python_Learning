from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return HttpResponse('<h1>Hi there, this is our first view for the Poll</h1>')

