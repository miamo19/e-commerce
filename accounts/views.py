from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

User = get_user_model()

def signup(request):
    if request.method == "POST":
        #handle the form in signu
        username = request.POST.get("username")
        password = request.POST.get("password")
        email  = request.POST.get("email")
        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email)
        login(request, user)
        return redirect('index')
    return render(request, "accounts/signup.html", {})

def login_user(request):
    #connect user to his account
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, "accounts/signIn.html", {})

def logout_user(request):
    logout(request)
    return redirect('index')