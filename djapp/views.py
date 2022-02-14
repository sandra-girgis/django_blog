from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='login')
def home(request):
    return render(request,'djapp/home.html')


       
       



    