from django.shortcuts import render, redirect
from Supplier.models import Suppliers
from django.contrib import messages

# View to display all suppliers
def SuppliersList(request):
    sData = Suppliers.objects.all()  # Fetching all suppliers
    return render(request, "Suppliers/supplyindex.html", {"supplierData": sData})

# View to add a new supplier
def AddSupplier(request):
    if request.method == "POST":
        # Collecting form data
        name = request.POST.get("name", "").strip()
        mobile_no = request.POST.get("mobile_no", "").strip()
        email = request.POST.get("email", "").strip()
        gst_no = request.POST.get("gst_no", "").strip()
        pan_no = request.POST.get("pan_no", "").strip()
        opening_balance = request.POST.get("opening_balance", "").strip()
        group_type = request.POST.get("group_type", "").strip()
        billing_address = request.POST.get("billing_address", "").strip()
        shipping_address = request.POST.get("shipping_address", "").strip()
        city = request.POST.get("city", "").strip()
        credit_limit = request.POST.get("credit_limit", "").strip()
        credit_period = request.POST.get("credit_period", "").strip()
        supplier_barcode = request.POST.get("supplier_barcode", "").strip()

        # Save the new supplier
        new_supplier = Suppliers(
            name=name,
            mobile_no=mobile_no,
            email=email,
            gst_no=gst_no,
            pan_no=pan_no,
            opening_balance=opening_balance or 0,
            group_type=group_type,
            billing_address=billing_address,
            shipping_address=shipping_address,
            city=city,
            credit_limit=credit_limit or 0,
            credit_period=credit_period or 0,
            supplier_barcode=supplier_barcode,
        )
        new_supplier.save()
        messages.success(request, "Supplier added successfully!")

        # Redirect to the supplier list page after adding
        return redirect(SuppliersList)

    return render(request, "Suppliers/supplyedit.html")

# View to edit an existing supplier
def editSupplier(request, id):
    sData = Suppliers.objects.get(id=int(id))  # Get supplier data by ID
    if request.method == "GET":
        context = {
            "sData": sData
        }
        return render(request, "Suppliers/supplyedit.html", context)
    else:
        # Collecting updated data from form
        name = request.POST.get("name").strip()
        mobile_no = request.POST.get("mobile_no").strip()
        email = request.POST.get("email").strip()
        gst_no = request.POST.get("gst_no").strip()
        pan_no = request.POST.get("pan_no").strip()
        opening_balance = request.POST.get("opening_balance").strip()
        group_type = request.POST.get("group_type").strip()
        billing_address = request.POST.get("billing_address").strip()
        shipping_address = request.POST.get("shipping_address").strip()
        city = request.POST.get("city").strip()
        credit_limit = request.POST.get("credit_limit").strip()
        credit_period = request.POST.get("credit_period").strip()
        supplier_barcode = request.POST.get("supplier_barcode").strip()
        
        # Updating supplier data
        sData.name = name
        sData.mobile_no = mobile_no
        sData.email = email
        sData.gst_no = gst_no
        sData.pan_no = pan_no
        sData.opening_balance = opening_balance or 0
        sData.group_type = group_type
        sData.billing_address = billing_address
        sData.shipping_address = shipping_address
        sData.city = city
        sData.credit_limit = credit_limit or 0
        sData.credit_period = credit_period or 0
        sData.supplier_barcode = supplier_barcode
        
        sData.save()
        messages.success(request, "Supplier details updated successfully!")
        return redirect(SuppliersList)

# View to delete a supplier
def deleteSupplier(request, id):
    sData = Suppliers.objects.get(id=int(id))
    sData.delete()
    messages.success(request, "Supplier deleted successfully!")
    return redirect(SuppliersList)




