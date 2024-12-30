from django.shortcuts import render
from Customer.models import Customer

def posdashboard(request):
    # Fetch customer data
    cData = Customer.objects.all()

    return render(request, "Pos/posindex.html",{"customerData": cData})  # Render the same template


