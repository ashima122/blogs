from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from new_blog.forms import BlogForm  
from new_blog.models import blog,profile
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

def register(request):
    if request.POST and request.FILES:  
        username = request.POST['username']
        password = request.POST['password']
        profile_Pic = request.FILES['profile_pic']
        new_user =User.objects.create(username=username,password=make_password(password))
        profile.objects.create(user_id=new_user.id,profile_pic=profile_Pic)
        messages.success(request, 'User registered Successfully')
        return redirect('/login')  
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        print("POSTT",request.POST['username'],  request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user,"user")
        if user is not None:
            login(request, user)
            messages.success(request, 'User login Successfully')
            return redirect('/')
        else:
            messages.error(request,'Error')
            return render(request, 'login.html',{'message':"Invalid Credentials"})
    return render(request, 'login.html')

@login_required(login_url="/login")
def file_new(request):
    if request.method == "POST":  
        form = BlogForm(request.POST)  
        if form.is_valid():  
            title = form.cleaned_data.get('title') 
            content = form.cleaned_data.get('content') 
            blogg =blog.objects.create(title=title,content=content,user_id=request.user.id)
            blogg.save()
            messages.success(request, 'Blog Created Successfully')
            return redirect('/')  

        else:  
            messages.error(request,'Error')
            return render(request, 'add_blog.html')
    
    return render(request, 'add_blog.html')

@login_required(login_url="/login")
def show(request):  
    blogs = blog.objects.all().order_by('-id')  
    get_pic = profile.objects.filter(user_id=request.user).get()
    return render(request,"index.html",{'blog':blogs,'img':get_pic})  

@login_required(login_url="/login")
def edit(request, id):  
    blogs = blog.objects.get(id=id)  
    form = BlogForm(request.POST)  
    if form.is_valid():  
        title = form.cleaned_data.get('title') 
        content = form.cleaned_data.get('content') 
        blogs.content =content
        blogs.title=title
        now=datetime.datetime.now()
        blogs.updated_date=  now.strftime("%Y-%m-%d")
        blogs.save()  
        messages.success(request, 'Blog Updated Successfully')
        return redirect("/")  
    return render(request,'edit.html', {'blogs':blogs})  

@login_required(login_url="/login")
def update(request, id):  
    blogs = blog.objects.get(id=id)  
    get_pic = profile.objects.filter(user_id=request.user).get()
    return render(request, 'content.html',{'blogs':blogs,'img':get_pic})  

@login_required(login_url="/login")
def destroy(request, id):  
    employee = blog.objects.get(id=id)  
    employee.delete()  
    messages.success(request, 'Blog Deleted Successfully')
    return redirect("/")  

def logout_user(request):
    logout(request)
    messages.success(request, 'User logout Successfully')
    return redirect('/login')