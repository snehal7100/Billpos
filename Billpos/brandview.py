
from django.shortcuts import render,redirect
from Brand.models import BrandForm
from django.contrib import messages
def Brands(request):
    bData = BrandForm.objects.all()
    bdata={
        "bData":bData
    }
    return render(request,"Brand/index.html",bdata)

# def BrandView(request,id):
#     bData = BrandForm.objects.all()
#     print(id)
#     bData={
#         "bData":bData,
#         "id":int(id),
        
#     }
#     return render(request,"Brand/view.html",bData)

def editBrand(request,id):
    bData= BrandForm.objects.get(id=int(id))
    if request.method == "GET":
        bData={
        "bData":bData,
    }
        return render(request,"Brand/edit.html",bData)
    else:
        name = request.POST.get("bname")
        img= request.FILES.get("img")
        bData.bname=name
        bData.img=img  
        bData.save()
        return redirect(Brands)
    
def delete(request,id):
    bData= BrandForm.objects.get(id=int(id))
    bData.delete() 
    return redirect(Brands)




def AddBrand(request):
    if request.method == "GET":
        return render(request, "Brand/addform.html")
    else:
        name = request.POST.get("bname").strip()
        img = request.FILES.get("img")
       

        if not name:
            messages.error(request, "Brand Name is required.")
            return render(request, "Brand/addform.html")



        if BrandForm.objects.filter(bname__iexact=name).exists():
            messages.error(request, "Duplicate entry not allowed! Brand name already exists.")
            return render(request, "Brand/addform.html")

        saveData = BrandForm(
            bname=name,
            img=img,
           
        )
        saveData.save()
        messages.success(request, "Brand added successfully!")
        return redirect(Brands)
