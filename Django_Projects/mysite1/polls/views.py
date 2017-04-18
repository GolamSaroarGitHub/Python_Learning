from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll
def home(request):

    latest_poll_list=Poll.objects.all().order_by('-pub_date')[:5]
    output=','.join([p.question for p in latest_poll_list])
    return HttpResponse(output)



def detail(request,poll_id):

    return HttpResponse("<h1>You are looking at %s.</h1>" % poll_id)



def result(request,poll_id):
    return HttpResponse("<h1>You are looking at the result of %s.</h1>" % poll_id)


def vote(request,poll_id):
    return HttpResponse("<h1>You are voting at %s.</h1>" % poll_id)
