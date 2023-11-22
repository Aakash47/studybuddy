from django.shortcuts import render, HttpResponse, redirect
from user import forms as user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return HttpResponse("hello world")

def registeruser(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = user_form.CreateUserForm()

    if request.method=="POST":
        form = user_form.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account has been Created for {form.cleaned_data.get('username')}")
            return redirect('home')
    context={
        "form":form
    }
    return render(request, "user/register.html", context=context)

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error=(request, "Username or password is incorrect")
    
    return render(request, "user/login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')