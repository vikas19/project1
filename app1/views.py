from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hai(request):
    return HttpResponse('This is first fbv')

def ab(request):
    return HttpResponse('No errors')