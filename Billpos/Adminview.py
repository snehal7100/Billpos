from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# View Profile
@login_required
def view_profile(request):
    return render(request, 'profile/view.html', {'user': request.user})

# Edit Profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('view_profile')
    return render(request, 'profile/edit.html', {'user': request.user})

# Logout User
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
