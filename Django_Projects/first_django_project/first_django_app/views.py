from django.http import HttpResponse



def index(request):
    return HttpResponse('<h1>Hi this is our first page</h1>')