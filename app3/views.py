from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app3_hai(request):
    return HttpResponse('app3 response')
