from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home, name='home' ) ,
    # path('add',views.addstudent, name='st-add'),
    path('register/', views.register, name='register' ) ,
    path('login/', views.login, name='login' ) ,
]