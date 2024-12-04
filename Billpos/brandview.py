
from django.shortcuts import render,redirect
from Brand.models import BrandForm
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