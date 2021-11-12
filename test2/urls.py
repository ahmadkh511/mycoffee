from typing import Pattern
from django.urls import path
from .import views


urlpatterns = [

    path('' , views.index2 , name=('index2')),
    path('my1', views.my1, name='my1' ),
    



]







