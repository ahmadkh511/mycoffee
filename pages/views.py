from django.http.response import HttpResponseNotModified
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product  # استيراد موديل من تطبيق اخر = products هو اسم التطبيق =   = product  هو  اسم الموديل

# Create your views here.

def index (request):

    #return HttpResponse ('<H1> this is Home page</H1>') يقراء من httprespons

    context = {  #  هproducts و نفسه الموجود في   فيو      

        'yy':Product.objects.all()  #product هو اسم الموديل
    }
    return render (request , 'pages/index.html',context)  # يقراء من الفيل تبع التمبلت


def about (request):
   # return HttpResponse ('<h1> this is about</h1>')

    return render (request , 'pages/about.html')


def coffee (request):
    return render (request , 'pages/coffee.html')
    


