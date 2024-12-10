# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout
# from Admin.models import Adminn

# # View Profile
# @login_required
# def view_profile(request):
#     return render(request, 'profile/view.html', {'user': request.user})

# # Edit Profile
# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         user = request.user
#         user.first_name = request.POST.get('first_name')
#         user.last_name = request.POST.get('last_name')
#         user.email = request.POST.get('email')
#         user.save()
#         return redirect('view_profile')
#     return render(request, 'profile/edit.html', {'user': request.user})

# # Logout User
# @login_required
# def logout_user(request):
#     logout(request)
#     return redirect('login')

# # Admin View (Custom Function)
# def AdminV(request, id):
#     aData = Adminn.objects.all()  # Fetch all data from Adminn model
#     admin_data = Adminn.objects.get(id=id)  # Get a specific admin by id
#     print(id)  # Debugging line to print the `id` in console
#     bData = {
#         "aData": aData,
#         "admin_data": admin_data,  # Pass the specific admin data
#         "id": int(id),
#     }
#     return render(request, "admin/view.html", bData)


