from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.

def index2 (request):
    return HttpResponse ('<h1> index2 from test2</h1>')




def my1 (request):
    return HttpResponse ('<h1> MY 1 FROM TEST2</h1>')
