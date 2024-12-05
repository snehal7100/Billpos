
from django.shortcuts import render,redirect
from Brand.models import BrandForm
from django.contrib import messages

def Brands(request):
    bData = BrandForm.objects.all()
    bdata={
        "bData":bData
    }
    return render(request,"Brand/index.html",bdata)

def BrandView(request,id):
    bData = BrandForm.objects.all()
    print(id)
    bData={
        "bData":bData,
        "id":int(id),
        
    }
    return render(request,"Brand/view.html",bData)

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
    if request.method == "POST":
        name = request.POST.get("bname", "").strip()
        img = request.FILES.get("img")

        # Server-side validation
        if not name or not img:
            messages.error(request, "Both Brand Name and Brand Image are required.")
            return render(request, "Brand/addform.html")

        # Check if brand name already exists
        if BrandForm.objects.filter(bname__iexact=name).exists():
            messages.error(request, "Brand Name already exists. Please choose a different name.")
            return render(request, "Brand/addform.html")

        # Save the new brand
        BrandForm.objects.create(bname=name, img=img)
        messages.success(request, "Brand added successfully!")
        return redirect("brand-list")

    return render(request, "Brand/addform.html")



