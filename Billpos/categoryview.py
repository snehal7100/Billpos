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
    categoryData = Category.objects.get(id=id)
    if request.method == 'GET':
        data = {
            "categoryData":categoryData,
        }
        return render(request, "Category/edit.html",data)
    else:
        name = request.POST.get("c_name")
        img = request.FILES.get("c_img")
        img1 = request.FILES.get("B_img")

        categoryData.c_name= name,
        categoryData.c_img= img,
        categoryData.B_img= img1,
        categoryData.save()
        return redirect(category)
    

def delete(request,id):
    categoryData = Category.objects.get(id=int(id))
    categoryData.delete()
    return redirect(category)


def category_form(request):
    if request.method == "POST":
        c_name = request.POST.get('c_name', 'unique=True').strip()
        c_img = request.FILES.get('img')
        B_img = request.FILES.get('img1')  
  

        if not c_name or not c_img or not B_img:
            messages.error(request, "Both category Name and category Image and banner Image are required.")
            return render(request, 'category-list')

    
        messages.success(request, "Category added successfully!")
        return redirect('category-list')  

    return render(request, 'category-list')


    
    





