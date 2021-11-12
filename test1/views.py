from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse ('<H1> PYTHON befor android </H1>')

def my1(request):
    return HttpResponse('<h1> my 1 </h1>')

def my2(request):
    return HttpResponse ('<h2> my 2</h2>')

def my3(request):
    return HttpResponse ('<h3> my 3</h3>')

