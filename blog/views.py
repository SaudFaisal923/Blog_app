from django.shortcuts import render,redirect
from .models import Profile,Blog,comments
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .Forms import LoginForm,CreateBlogForm,CommentForm
from django.urls import reverse
from django.http import HttpResponse


def register(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form=UserCreationForm()
		return render (request,"blog/signup.html",{"form":form})

def Login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('blogs')
            else:
                return HttpResponseRedirect(reverse('login'))
    else:
        form=LoginForm()
        return render(request,'blog/signup.html',{'form':form})
def create_blog(request):
	if request.method=='POST':
		form=CreateBlogForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.user=request.user
			post.save()
			return redirect('blogs')
	else:
		form=CreateBlogForm()
		return render(request,'blog/create_blog.html',{'form':form})

def Blogs(request):
    obj=Blog.objects.all()
    return render(request,'blog/blogs.html',{'obj':obj})
def View_blog(request,id):
	try:
		obj=Blog.objects.get(id=id)
		comm=comments.objects.filter(blog=obj)
		form=CommentForm()
	except Blog.DoesNotExist:
		return HttpResponse("page not found")
	if request.method=="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			comm=form.save(commit=False)
			comm.user=request.user
			comm.blog=obj
			comm.save()
			return redirect('viewblog',id=id)
	# else:
	# 	try:
	# 		obj=Blog.objects.get(id=id)
	# 		comm=comments.objects.filter(blog=obj)
	# 		form=CommentForm()
	# 	except Blog.DoesNotExist:
	# 		return HttpResponse("page not found")
	return render(request,'blog/blog_view.html',{'obj':obj,'form':form,'comm':comm})

def MyBlogs(request):
	obj=Blog.objects.filter(user=request.user)
	return render(request,'blog/myblogs.html',{'obj':obj})
