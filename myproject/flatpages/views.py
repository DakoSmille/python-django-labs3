from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Привет, Мир!')

def hello(request):
    return HttpResponse('Привет, Мир!')
