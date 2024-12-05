from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if fields are filled
        if not email or not password:
            messages.error(request, "Both email and password are required.")
            return render(request, 'Component/index.html')

        # Explicitly check if the email and password match the required values
        if email == "sukhdi@gmail.com" and password == "sukhda@":
            # Successful login, redirect to the admin dashboard
            messages.success(request, f"Welcome back, Admin!")
            return redirect('/admin/')  # Redirect to Django admin or your admin dashboard URL
        else:
            # Invalid credentials, show error message and render login form again
            messages.error(request, "Invalid email or password.")
            return render(request, 'Component/index.html')

  
    return render(request, 'Component/index.html')
