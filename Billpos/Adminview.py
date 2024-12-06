from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from Admin.models import Adminn

# @login_required
# def view_profile(request):
#     return render(request, 'Adminprofile/view.html', {'user': request.user})

def view_profile(request,id):
    bData = Adminn.objects.all()
    print(id)
    bData={
        "bData":bData,
        "id":int(id),
        
    }
    return render(request,"Adminprofile/view.html",bData)




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

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
