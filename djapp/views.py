from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django import forms
from .models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import User


#auth views.
def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username= name, password =passwd)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
                
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'djapp/login.html')



def signoutPg(request):
    logout(request)
    return redirect('login')




def register(request):
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST)  #input from user
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')



        context = {'signup_form': signup_form}
        return render(request, 'djapp/register.html', context)

   

def home(request):
    categoryyy = Category.objects.all()
    post = Post.objects.all()


    if request.user.id != None:
        categori = CategoryMembership.objects.filter(userr=request.user.id)
        context = {'categories': categoryyy,'mycategory':categori,'posts':post }
        return render(request,'djapp/home.html',context=context)
    else:
        context = {'categories': categoryyy,'posts':post}
        return render(request,'djapp/home.html',context=context)


       
@login_required(login_url='login')       
def subscribe(request,id):
    userr = request.user
    categoryy = Category.objects.get(id=id)
    adding_to_model = CategoryMembership(userr=userr,categoryy=categoryy)
    adding_to_model.save()
    return redirect('home')

@login_required(login_url='login')       
def unsubscribe(request,id):
    userr = request.user
    categoryy = Category.objects.get(id=id)
    CategoryMembership.objects.filter(userr=userr,categoryy=categoryy).delete()
    return redirect('home')

