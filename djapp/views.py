from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth

# Create your views here.
def home(request):
    return render(request,'djapp/home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST) #input from user
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')


        context = {'signup_form': signup_form}
        return render(request, 'djapp/register.html', context)
        
def login(request):
    context={}
    return render (request,'djapp/login.html',context)