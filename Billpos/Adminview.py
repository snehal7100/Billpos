from django.shortcuts import render,redirect
from Admin.models import Adminn

def AdminV(request,id):
    aData = Adminn.objects.all()
    print(id)
    bData={
        "aData":aData,
        "id":int(id),
        
    }
    return render(request,"admin/view.html",bData)