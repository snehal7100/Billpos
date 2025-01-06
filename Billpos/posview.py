from django.shortcuts import render
from Customer.models import Customer
from Product.models import ProductModel

def posdashboard(request):
    # Fetch customer and product data
    cData = Customer.objects.all()  # Fetch all customer records
    pData = ProductModel.objects.all()  # Fetch all product records
    return render(request, "Pos/posindex.html", {"customerData": cData, "productData": pData})
