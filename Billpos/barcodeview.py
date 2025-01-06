from django.shortcuts import render

from Product.models import ProductModel

def BarcodePrint(request):
    pData = ProductModel.objects.all()  # Fetch all product records
    return render(request, "Pos/posindex.html", {"productData": pData})
