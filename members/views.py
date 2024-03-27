from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def members(request):
    return HttpResponse("Hello world!!!")

def wish(request):
    message = "<h1>Hi buddy, How are you</h1>"
    return HttpResponse(message)
