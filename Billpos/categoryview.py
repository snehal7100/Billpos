from django.shortcuts import render,redirect
from category.models import Category
from django.contrib import messages


def category(request):
    categoryData = Category.objects.all()
    data = {
    "categoryData":categoryData
    }   
    return render(request,'Category/index.html',data)

def addcategory(request):
    if request.method == "GET":
        return render(request,"Category/add.html")
    else:
        name = request.POST.get("c_name")
        img = request.FILES.get("c_img")
        img1 = request.FILES.get("B_img")
        saveData = Category(
            c_name=name,
            c_img=img,
            B_img=img1,
           )
        saveData.save()
        return redirect(category)
    


def categoryview(request,id):
    categoryData = Category.objects.all()
    print(id)
    data = {
    "categoryData":categoryData,
    "id":int(id),
    }
    return render(request,'Category/view.html',data)

<<<<<<< HEAD
def editcategory(request,id):
    categoryData= Category.objects.get(id=int(id))
    if request.method == 'GET':
        categoryData = {
            "categoryData":categoryData,
        }
        return render(request, "Category/edit.html",categoryData)
=======
def editcategory(request, id):
    categoryData = Category.objects.get(id=id)
    if request.method == 'GET':
        data = {
            "categoryData": categoryData,
        }
        return render(request, "Category/edit.html", data)
>>>>>>> 92d7f0aed4b71b0d387a4f4ec8124ffbdc16165e
    else:
        name = request.POST.get("c_name")
        img = request.FILES.get("c_img")
        img1 = request.FILES.get("B_img")

        # Assign values directly without a trailing comma
        categoryData.c_name = name
        if img:  # Only update if a new file is uploaded
            categoryData.c_img = img
        if img1:  # Only update if a new file is uploaded
            categoryData.B_img = img1
        
        categoryData.save()
        return redirect(category)
    

def delete(request,id):
    categoryData = Category.objects.get(id=int(id))
    categoryData.delete()
    return redirect(category)




    
    





