from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home, name='home' ) ,
    path('add',views.addstudent, name='st-add'),

]