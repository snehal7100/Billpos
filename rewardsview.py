from django.shortcuts import render, redirect, get_object_or_404
from Reward.models import RewarsPoints
from django.contrib import messages

def Rewards(request):
    rData = RewarsPoints.objects.all()
    return render(request, "Rewards/index.html", {"rData": rData})

def editRewards(request, id):
    rData = get_object_or_404(RewarsPoints, id=id)

    if request.method == "POST":
        minrange = request.POST.get("minrange")
        maxrange = request.POST.get("maxrange")
        points = request.POST.get("points")

        if not minrange or not maxrange or not points:
            messages.error(request, "All fields are required.")
            return redirect(f"/rewards-edit/{id}")

        # Update the reward
        rData.minrange = minrange
        rData.maxrange = maxrange
        rData.points = points
        rData.save()

        messages.success(request, "Reward updated successfully.")
        return redirect(Rewards)
    else:
        return render(request, "Rewards/edit.html", {"rData": rData})

def AddRewards(request):
    if request.method == "POST":
        minrange = request.POST.get("minrange", "").strip()
        maxrange = request.POST.get("maxrange", "").strip()
        points = request.POST.get("points", "").strip()

        if not minrange or not maxrange or not points:
            messages.error(request, "All fields are required.")
            return redirect("/rewards-add/")

        if RewarsPoints.objects.filter(minrange=minrange, maxrange=maxrange).exists():
            messages.error(request, "A reward with the same range already exists.")
            return redirect("/rewards-add/")

        RewarsPoints.objects.create(
            minrange=minrange,
            maxrange=maxrange,
            points=points,
        )
        messages.success(request, "Reward added successfully!")
        return redirect(Rewards)

    messages.error(request, "Invalid request method.")
    return redirect(Rewards)

def delete(request, id):
    rData = get_object_or_404(RewarsPoints, id=id)
    rData.delete()
    messages.success(request, "Reward deleted successfully.")
    return redirect(Rewards)
