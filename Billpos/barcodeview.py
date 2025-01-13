from django.shortcuts import render
from Product.models import ProductModel
from category.models import Category 

def Barcodes(request):
    category_query = "SELECT * FROM tbl_category"
    categoryData = Category.objects.raw(category_query)
    pData = ProductModel.objects.all()  
    context = {
        "productData": pData,
        "categoryData": categoryData
    }
    return render(request, "Barcode/index.html", context)