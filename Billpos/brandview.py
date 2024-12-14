
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
    if request.method == "POST":
       
        name = request.POST.get("bname").strip()
        img = request.FILES.get("img")

        print("Brand Name:", name)  # Debugging line
        print("Image:", img)  # Debugging line
        
        # Validate the Brand Name
        if not name:
            messages.error(request, "Brand Name is required.")
            return render(request, "Brand/addform.html")  # Re-render the form on error

        # Check if the brand name already exists (case-insensitive check)
        if BrandForm.objects.filter(bname__iexact=name).exists():
            messages.error(request, "Duplicate entry not allowed! Brand name already exists.")
            return render(request, "Brand/addform.html")  # Re-render the form on error

        # Save the new brand data to the database
        saveData = BrandForm(
            bname=name,
            img=img,
        )
        saveData.save()

        # Show success message and redirect to the brand list or any other page
        messages.success(request, "Brand added successfully!")
        return redirect(Brands)  # Replace 'brands_list' with the name of your brands listing view
