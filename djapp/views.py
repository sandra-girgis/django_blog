from pickle import TRUE
from pymysql import NULL
from .forms import *
from .models import *
from django import forms
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User
from django.contrib.auth import login, logout, authenticate
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
                signup_form.instance.is_staff = True
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
        x = []
        cat = CategoryMembership.objects.filter(userr=request.user.id)
        for i in cat :
            x.append(i.categoryy.Name)      
        context= {'categories': categoryyy,'my_category':x,'posts':post }
        return render(request,'djapp/home.html',context)
    else:
        context = {'categories': categoryyy,'posts':post}
        return render(request,'djapp/home.html',context)
    
        
def showPost(request, p_id):
    post = Post.objects.get(id = p_id)
    user = request.user.id
    if request.user.id !=None:
        pos = Postlike.objects.filter(User_id=user,Post_id=post.id,Islike=True,Isdislike=False)
        # pos1 = Postlike.objects.filter(User_id=user,Post_id=post.id,Islike=False,Isdislike=True)
        return render(request,'djapp/post.html',{'Post':post,'my_post':pos})
    else:    
     context = { 'Post' : post }
     return render(request,'djapp/home.html',context)

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

@login_required(login_url='login')       
def like(request,id):
    user = request.user
    post = Post.objects.get(id=id)
    adding_to_model = Postlike(User_id=user,Post_id=post,Islike=True,Isdislike=False)
    adding_to_model.save()
    return redirect('home')    

@login_required(login_url='login')       
def unlike(request,id):
    user = request.user
    post = Post.objects.get(id=id)
    Postlike.objects.filter(User_id=user,Post_id=post,Islike=True,Isdislike=False).delete()
    return redirect('home')    
# @login_required(login_url='login')       
# def dislike(request,id):
#     user = request.user
#     post = Post.objects.get(id=id)
#     adding_to_model = Postlike(User_id=user,Post_id=post,Isdislike=True,Islike=False)
#     adding_to_model.save()
#     return redirect('home')  

# @login_required(login_url='login')       
# def canceldislike(request,id):
#     user = request.user
#     post = Post.objects.get(id=id)
#     Postlike.objects.filter(User_id=user,Post_id=post,Islike=False,Isdislike=True).delete()
#     return redirect('home')        
##########
def addUser(request):
    if request.method == "POST":
        form = UForm(request.POST)
        # date
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            context = { 'form' : form }
            return render(request,'djapp/u_add.html',context)
    else:
        form = UForm()
        context = { 'form' : form }
        return render(request,'djapp/u_add.html',context)

def delUser(request,u_id):
    user = User.objects.get(id = u_id)
    user.delete()
    return redirect('blog')

def addPost(request):
    if request.method == "POST":
        form = PForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            context = { 'form' : form }
            return render(request,'djapp/p_add.html',context)
    else:
        form = PForm()
        context = { 'form' : form }
        return render(request,'djapp/p_add.html',context)


def manageBlog(request):
    if request.user.is_superuser:
        users = User.objects.all()
        posts = Post.objects.all()
        categories = Category.objects.all()
        words = Word.objects.all()
        context = { 'users' : users , 'posts' : posts , 'categories' : categories , 'words' : words}
        return render(request,'djapp/blog.html',context)
    else:
        return render(request,'djapp/home.html')


# def post_view(request):
#     qs = Post.objects.all()
#     user = request.user

#     context = {
#         'qs':qs,
#         'user':user,
#     }

#     return render(request,'djapp/post.html',context)