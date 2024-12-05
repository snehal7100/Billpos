from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('passw')
        if not username or not password:
            messages.error(request, "Both email and password are required.")
            return render(request, 'Component/index.html')
        if username == "admin@gmail.com" and password == "admin":
            messages.success(request, f"Welcome back, Admin!")
            return redirect('/index/')  
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'Component/index.html')
        
    return render(request, 'Component/index.html')
