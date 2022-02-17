from .forms import *
from .models import *
from django import forms
from .forms import UserForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse
from django.contrib.auth.admin import User
from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Register page
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

# Log in page
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

# Sign out function
def signoutPg(request):
    logout(request)
    return redirect('home')

# Home page
def home(request):
    categoryyy = Category.objects.all()
    post = Post.objects.all()
    if request.user.id != None:
        x = []
        cat = CategoryMembership.objects.filter(userr=request.user.id)
        for i in cat :
            x.append(i.categoryy.Name)      
        context= {'categories': categoryyy,'my_category':x,'posts':post, 'u_id': request.user.id }
        return render(request,'djapp/home.html',context)
    else:
        context = {'categories': categoryyy,'posts':post}
        return render(request,'djapp/home.html',context)

# Post page
def showPost(request, p_id):
    # find post by post id
    post = Post.objects.get(id = p_id)
    # count post likes
    post.Likes = Postlike.objects.filter(Post_id=p_id,Islike=True).count()
    # count post dislikes
    post.Dislikes = Postlike.objects.filter(Post_id=p_id,Isdislike=True).count()
    # save counters in post db
    post.save()
    context = { 'Post' : post ,'Likes_no': post.Likes,'Dislikes_no': post.Dislikes}# ,'like':Islike,'dislike':Isdislike
    return render(request,'djapp/post.html',context)

# Manage blog page
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

# Category functions
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

# User functions
@login_required(login_url='login')  
def addUser(request):
    user_form = UForm()
    if request.method == "POST":
        user_form = UForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('blog')
    context = { 'form' : user_form }
    return render(request,'djapp/u_add.html',context)

def editPost(request, p_id):
    post = Post.objects.get(id = p_id)
    if request.method == "POST":
        form = PForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = PForm(instance = post)
    context = {'form': form}
    return render(request, 'djapp/p_add.html', context)

@login_required(login_url='login')  
def delUser(request,u_id):
    user = User.objects.get(id = u_id)
    user.delete()
    return redirect('blog')

@login_required(login_url='login')  
def editUser(request,u_id):
    user = User.objects.get(id = u_id)
    if request.method == "POST":
        form = UForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('blog')
    form = UForm(instance=user)
    context = { 'form' : form }
    return render(request,'djapp/u_add.html',context)

# Post functions
@login_required(login_url='login')  
def addPost(request):
    form = PForm()
    if request.method == 'POST':

        form = PForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form' : form }
    return render(request, 'djapp/p_add.html', context)

# Post page
def showPost(request, p_id):
    # find post by post id
    post = Post.objects.get(id = p_id)
    # count post likes
    post.Likes = Postlike.objects.filter(Post_id=p_id,Islike=True).count()
    # count post dislikes
    post.Dislikes = Postlike.objects.filter(Post_id=p_id,Isdislike=True).count()
    # save counters in post db
    post.save()
    context = { 'Post' : post ,'Likes_no': post.Likes,'Dislikes_no': post.Dislikes}# ,'like':Islike,'dislike':Isdislike
    return render(request,'djapp/post.html',context)

# search posts with tags or category
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(Tags__Name__icontains=searched) | Post.objects.filter(Post_category__Name__icontains=searched)
        return render(request,'djapp/search.html',{'searched':searched,'Posts':posts})
    else:
        return render(request,'djapp/search.html')

# def categoryPosts(request,c_id):
#     pass

#category's functions 
def addCatagory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form' : form }
    return render(request, 'djapp/Cat_add.html', context)


def editCatagory(request, cat_id):
    category = Category.objects.get(id = cat_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = CategoryForm(instance = category)
    context = {'form': form}
    return render(request,'djapp/CategoriesForm.html', context)


def delCatagory(requset, cat_id):
    category = Category.objects.get(id = cat_id)
    category.delete()
    return redirect('blog') 


#undesired words function 

def addWord(request):
    form = BadWordsForm()
    if request.method == 'POST':
        form = BadWordsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form' : form }
    return render(request, 'djapp/Bad_Words_Form.html', context)


def editWord(request, w_id):
    word = Word.objects.get(id = w_id)
    if request.method == "POST":
        form = BadWordsForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('blog')

    form = BadWordsForm(instance = word)
    context = {'form': form}
    return render(request,'djapp/Bad_Words_Form.html', context)


def delWord(requset, w_id):
    word = Word.objects.get(id = w_id)
    word.delete()
    return redirect('blog') 


