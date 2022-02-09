from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request,'djapp/home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

    context = { 'form': form}
    return render(request, 'djapp/register.html', context)

def login(request):
    context= {}
    return render(request, 'djapp/login.html', context)