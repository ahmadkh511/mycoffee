from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('my1' , views.my1 , name = 'my1'),
    path('my2' , views.my2 , name = 'my2'),
    path('my3' , views.my3 , name='my3'),
]
