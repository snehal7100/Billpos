from django.shortcuts import render
from Product.models import ProductModel

def Barcodes(request):
    pData = ProductModel.objects.all()  
    return render(request, "Barcode/index.html", {"productData": pData})