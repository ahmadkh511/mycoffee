from django.urls import path
from . import views

urlpatterns = [

    path ('', views.products , name='products'),
    path ( '<int:pro_id>' , views.product , name='product' ),#اذا كتبنا كلمة بروتكت في البداية اي سوف يكون رابط للذهاب الى الصفحة \\pro_id نستقبلها  بي  views
    path ('search' ,views.search , name= 'search'),


    
]

