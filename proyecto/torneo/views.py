from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo (request):
    return HttpResponse ('hola')