from django.shortcuts import render , redirect
from django.http import HttpResponse
# from django.form import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'djapp/home.html')

def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'djapp/register.html',context)
        
def login(request):
    context={}
    return render (request,'djapp/login.html',context)