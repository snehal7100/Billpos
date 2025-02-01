from django.shortcuts import render
from Product.models import ProductModel
from category.models import Category 
from Brand.models import BrandForm as Brand
from Taxes.models import Taxs as Tax

def Barcodes(request):
    category_query = "SELECT * FROM tbl_category"
    categoryData = Category.objects.raw(category_query)
    brand_query = "SELECT * FROM tbl_brand"
    bData = Brand.objects.raw(brand_query)
    taxes_query = "SELECT * FROM tbl_taxes"
    taxData = Tax.objects.raw(taxes_query)
    pData = ProductModel.objects.all()  
    context = {
        "productData": pData,
        "categoryData": categoryData,
        "bData": bData,  
        "taxData": taxData,
    }
    return render(request, "Barcode/index.html", context)



