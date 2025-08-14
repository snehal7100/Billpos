
from django.shortcuts import render, redirect, get_object_or_404
from payment.models import Payment
from django.contrib import messages

def payments(request):
    pdata = Payment.objects.all()
    pdata={
        "pdata":pdata
    }
    return render(request,"Payment/index.html",pdata)


def editpayment(request,id):
    pdata= Payment.objects.get(id=int(id))
    if request.method == "GET":
        pdata={
        "pdata":pdata,
    }
        return render(request,"Payment/edit.html",pdata)
    else:
        name = request.POST.get("pname")
        pdata.pname=name 
        pdata.save()
        return redirect(payments)
    
def delete(request, id):
    pdata = get_object_or_404(Payment, id=id)
    pdata.delete()
    messages.success(request, "Payment record deleted successfully.")
    return redirect(payments) 



def AddPayment(request):
    if request.method == "GET":
        return render(request, "Payment/addform.html")
    
    else:
        name = request.POST.get("pname").strip()
        
       

        if not name:
            messages.error(request, "Payment is required.")
            return render(request, "Payment/addform.html")



        if Payment.objects.filter(pname__iexact=name).exists():
            messages.error(request, "Duplicate entry not allowed! Payment already exists.")
            return render(request, "Payment/addform.html")

        saveData = Payment(
            pname=name,
            
           
        )
        saveData.save()
        messages.success(request, "Payment added successfully!")
        return redirect(payments)
