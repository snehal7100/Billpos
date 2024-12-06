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

def editcategory(request,id):
    categoryData= Category.objects.get(id=int(id))
    if request.method == 'GET':
        categoryData = {
            "categoryData":categoryData,
        }
        return render(request, "Category/edit.html",categoryData)

def editcategory(request, id):
    categoryData = Category.objects.get(id=id)
    if request.method == 'GET':
        data = {
            "categoryData": categoryData,
        }
        return render(request, "Category/edit.html", data)

    else:
        name = request.POST.get("c_name")
        img = request.FILES.get("c_img")
        img1 = request.FILES.get("B_img")

        categoryData.c_name = name
        if img:  
            categoryData.c_img = img
        if img1: 
            categoryData.B_img = img1
        
        categoryData.save()
        return redirect(category)
    

def delete(request,id):
    categoryData = Category.objects.get(id=int(id))
    categoryData.delete()
    return redirect(category)

def AddCategory(request):
    if request.method == "GET":
        return render(request, "Category/add.html")
    else:
        name = request.POST.get("c_name").strip()
        img = request.FILES.get("c_img")
        img1 = request.FILES.get("B_img")

        if not name:
            messages.error(request, "Category Name is required.")
            return render(request, "Category/add.html")

        if not img:
            messages.error(request, "Category Image is required.")
            return render(request, "Category/add.html")

        if not img1:
            messages.error(request, "Banner Image is required.")
            return render(request, "Category/add.html")

        if Category.objects.filter(c_name__iexact=name).exists():
            messages.error(request, "Duplicate entry not allowed! Category name already exists.")
            return render(request, "Category/add.html")

        saveData = Category(
            c_name=name,
            c_img=img,
            B_img=img1
        )
        saveData.save()
        messages.success(request, "Category added successfully!")
        return redirect('category-list')

