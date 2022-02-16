from .forms import *
from .models import *
from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.admin import User
from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'djapp/register.html', context)

def home(request):
    category = Category.objects.all()
    if request.user.id != None:
        x = []
        cat = CategoryMembership.objects.filter(user=request.user.id)
        for i in cat :
            x.append(i.category.Name)
        context = {'categories': category,'my_category':x}
        return render(request,'djapp/home.html',context=context)
    else:
        context = {'categories': category}
        return render(request,'djapp/home.html',context=context)

def subscribe(request,id):
    User = request.user
    category = Category.objects.get(id=id)
    adding_to_model = CategoryMembership(user=User,category=category)
    adding_to_model.save()
    return redirect('home')

def unsubscribe(request,id):
    User = request.user
    category = Category.objects.get(id=id)
    CategoryMembership.objects.filter(user=User,category=category).delete()
    return redirect('home')