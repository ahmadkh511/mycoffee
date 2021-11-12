from django.shortcuts import get_object_or_404, render # احضار الوبجيكت او صفحة لا يوجد
from datetime import datetime
from .models import Product  # استيراد ال كلاس الموجود في الموديل


# Create your views here.

#def products (request):
    #return render (request , 'products/products.html' , {
        
        #'my':'test' ,'to':'help'
        
        #})  # من بين هذه الاقواص نرسل كل ما نرير  الى صفحة  products.html

def products (request):

    pro = Product.objects.all()


    name  =None
    if 'searchname' in request.GET:
        name = request.GET ['searchname']
        if name :
            pro = pro.filter(name__icontains=name)

    context = {

        'yy': pro

        #'yy':Product.objects.all()   #product هو اسم الموديل
            
    }
    return render (request , 'products/products.html', context )

#=================================================================================


def product (request , pro_id):

    context = {

        'pro':get_object_or_404(Product , pk=pro_id)  # ال product  هو اسم الموديل الذي اريد ان احضر منه المعلومات-----يجب الانتباه للاسم اي حالة الحرف
    }
    return render (request , 'products/product.html', context)

#=============================================================================================================

def search (request):
    return render (request , 'products/search.html' )

    
   