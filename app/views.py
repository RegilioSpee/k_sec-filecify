from django.shortcuts import render,HttpResponse,redirect
from .forms import Video_form
from .models import Video
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    all_video=Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video uploaded succesfully')   
    else:
        form=Video_form()
    return render(request,'index.html',{"form":form,"all":all_video})

def registration(request):
    if request.method == "POST":
        user_form=UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Video uploaded succesfully')  
    else: 
        user_form=UserCreationForm()
        return render(request, 'registration.html',{'user_form':user_form})

def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd["username"],password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('<h1>Login succesfully</h1>')
                else: 
                    return HttpResponse('<h1>Disable account</h1>')
            else: 
                return HttpResponse('<h1>Invalid login</h1>')
        else: 
             login_form=LoginForm()
        return render(request, 'login.html',{'login_form':login_form})

