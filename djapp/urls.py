from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.home, name='home' ) ,
    path('register/', views.register, name='register' ) ,
    path('login/', views.loginPg, name='login' ) ,
    path('signout', views.signoutPg, name='signout'),
    path('subscribe/<int:id>',views.subscribe,name='subscribe-to-category'),
    path('unsubscribe/<int:id>',views.unsubscribe,name='unsubscribe-to-category') ,
]