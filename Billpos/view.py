from django.shortcuts import render,redirect
from django.contrib import messages
from Login.models import LoginForm


def Login(request):
    return render(request,"Component/index.html")

def Index(request):
    return render(request,"index.html")




def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if fields are filled
        if not email or not password:
            messages.error(request, "Both email and password are required.")
            return render(request, 'login.html')

        # Authenticate user by checking the database
        try:
            user = LoginForm.objects.get(uname=email, passw=password)
            # Successful login (Redirect or other logic can go here)
            messages.success(request, f"Welcome back, {user.uname}!")
            return redirect('/dashboard/')  # Redirect to a dashboard or home page
        except LoginForm.DoesNotExist:
            # If the user does not exist, show error and stay on the login page
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    # Render the login page if GET request
    return render(request, 'login.html')
