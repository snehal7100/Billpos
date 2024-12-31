from django.shortcuts import render, redirect
from Reward.models import RewarsPoints
from django.contrib import messages
from django.http import JsonResponse

def Rewards(request):
    rData = RewarsPoints.objects.all()
    rdata = {
        "rData": rData
    }
    return render(request, "Rewards/index.html", rdata)

def editRewards(request, id):
    rData = RewarsPoints.objects.get(id=int(id))
    if request.method == "GET":
        rData = {
            "rData": rData,
        }
        return render(request, "Rewards/edit.html", rData)
    else:
        minrange = request.POST.get("minrage")
        maxrange = request.POST.get("maxrange")
        points = request.POST.get("points")

        # Update the reward
        rData.minrage = minrange
        rData.maxrange = maxrange
        rData.points = points
        rData.save()
        return redirect(Rewards)


def AddRewards(request):
    if request.method == "POST":
        minrange = request.POST.get("minrange", "").strip()
        maxrange = request.POST.get("maxrange", "").strip()
        points = request.POST.get("points", "").strip()

        if not minrange or not maxrange or not points:
            return JsonResponse({"message": "All fields are required."}, status=400)

        if RewarsPoints.objects.filter(minrange=minrange, maxrange=maxrange).exists():
            return JsonResponse({"message": "A reward with the same range already exists."}, status=400)

        saveData = RewarsPoints(
            minrange=minrange,
            maxrange=maxrange,
            points=points,
        )
        saveData.save()
        return JsonResponse({
            "message": "Reward added successfully!",
            "data": {
                "id": saveData.id,
                "minrange": saveData.minrange,
                "maxrange": saveData.maxrange,
                "points": saveData.points
            }
        }, status=200)

    return JsonResponse({"message": "Invalid request method."}, status=405)


def delete(request, id):
    rData = RewarsPoints.objects.get(id=int(id))
    rData.delete()
    return redirect(Rewards)
