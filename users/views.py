from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")
        phone_number = request.POST.get("phone")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
            latitude=latitude,
            longitude=longitude
        )

        messages.success(request, "Account created successfully")
        return redirect("Disaster_main")   # make sure login url exists

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Disaster_main")  # change to your homepage name
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def Disaster_main(request):
    return render(request, "main_disaster_page.html")