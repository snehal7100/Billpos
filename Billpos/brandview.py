
from django.shortcuts import render, redirect, get_object_or_404
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

def editBrand(request, id):
    bData = get_object_or_404(BrandForm, id=id)
    if request.method == "GET":
        context = {
            "bData": bData,
        }
        return render(request, "Brand/edit.html", context)
    else:
        name = request.POST.get("bname")
        img = request.FILES.get("img")
        bData.bname = name
        if img:  # Update image only if a new one is uploaded
            bData.img = img
        bData.save()

        # Add success message
        messages.success(request, "Brand updated successfully!")
        return redirect(Brands)
def delete(request, id):
    bData = get_object_or_404(BrandForm, id=id)
    bData.delete()
    messages.success(request, "brand record deleted successfully.")
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
