from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.success(request, "Username or Password is incorrect")
    return render(request, "FasalUdyog_Users/login.html")

def logout_user(request):
    logout(request)