
from django.shortcuts import render,redirect
from Reward.models import RewarsPoints
from django.contrib import messages
def Rewards(request):
    rData = RewarsPoints.objects.all()
    rdata={
        "rData":rData
    }
    return render(request,"Rewards/index.html",rdata)

def editRewards(request,id):
    rData= RewarsPoints.objects.get(id=int(id))
    if request.method == "GET":
        rData={
        "rData":rData,
    }
        return render(request,"Rewards/edit.html",rData)
    else:
        minrage= request.POST.get("minrage")
        maxrange= request.POST.get("maxrange")
        points = request.POST.get("points")
       
        rData.minrage=minrage
        rData.maxrange=maxrange
        rData.points=points
     
        rData.save()
        return redirect(Rewards)
    


def AddRewards(request):
    if request.method == "POST":
        minrange = request.POST.get("minrange", "").strip()
        maxrange = request.POST.get("maxrange", "").strip()
        points = request.POST.get("points", "").strip()

        if not minrange or not maxrange or not points:
            messages.error(request, "All fields are required.")
            return redirect(Rewards)

        saveData = RewarsPoints(
            minrange=minrange,
            maxrange=maxrange,
            points=points,
        )
        saveData.save()
        messages.success(request, "Reward added successfully!")
        return redirect(Rewards)

    return render(request, "Rewards/addform.html")
    
def delete(request,id):
    rData= RewarsPoints.objects.get(id=int(id))
    rData.delete() 
    return redirect(Rewards) 