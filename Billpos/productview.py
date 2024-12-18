from django.shortcuts import render,redirect
from Product.models import ProductModel
from Brand.models import BrandForm as Brand
from django.contrib import messages
def Products(request):
    product_query = """
        SELECT * 
        FROM tbl_product
        INNER JOIN tbl_brand ON tbl_product.brand = tbl_brand.bid    
    """
    pData = ProductModel.objects.raw(product_query)

    brand_query = "SELECT * FROM tbl_brand"
    bData = Brand.objects.raw(brand_query)

    context = {
        "pData": pData,
        "bData": bData,  # Pass brand data to template
    }
    return render(request, "Product/index.html", context)


def EditProduct(request,id):
    pData= ProductModel.objects.get(id=int(id))
    if request.method == "GET":
        pData={
        "pData":pData,
    }
        return render(request,"product/edit.html",pData)
    else:
        name = request.POST.get("pname")
        hsncode = request.POST.get("hsncode")
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        tax = request.POST.get("tax")
        type = request.POST.get("taxtype")
        punit = request.POST.get("punit")
        aunit = request.POST.get("aunit")
        factor = request.POST.get("cfactor")
        price = request.POST.get("price")

        pData.pname=name
        pData.hsncode=hsncode
        pData.category=category
        pData.brand=brand
        pData.tax=tax
        pData.taxtype=type
        pData.punit=punit
        pData.aunit=aunit
        pData.cfactor=factor
        pData.price=price
        
        pData.save()
        return redirect(Products)
    
def delete(request,id):
    pData= ProductModel.objects.get(id=int(id))
    pData.delete() 
    return redirect(Products)


def AddProduct(request):
    if request.method == "GET":
        return render(request, "product/index.html")
    else:
        name = request.POST.get("pname").strip()
        hsncode = request.POST.get("hsncode").strip()
        category = request.POST.get("category").strip()
        brand = request.POST.get("brand", "").strip()

        tax = request.POST.get("tax").strip()
        type = request.POST.get("taxtype").strip()
        punit = request.POST.get("punit").strip()
        aunit = request.POST.get("aunit").strip()
        factor = request.POST.get("cfactor").strip()
        price = request.POST.get("price").strip()

        if not name:
            messages.error(request, "product Name is required.")
            return render(request, "product/index.html")
        
        if ProductModel.objects.filter(pname__iexact=name).exists():
            messages.error(request, "Duplicate entry not allowed! Product name already exists.")
            return render(request, "product/index.html")

        saveData = ProductModel(
            pname=name,
            hsncode=hsncode,
            category=category,
            brand=brand,
            tax=tax,
            taxtype=type,
            punit=punit,
            aunit=aunit,
            cfactor=factor,
            price=price,
        )
        saveData.save()
        messages.success(request, "Product added successfully!")
        return redirect(Products)
