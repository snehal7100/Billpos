from django.shortcuts import render, redirect
from Customer.models import Customer
from django.contrib import messages

def Customers(request):
    cData = Customer.objects.all()  # Fetching all customers
    return render(request, "Customers/Custindex.html", {"customerData": cData})

def AddCustomer(request):
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
        customer_barcode = request.POST.get("customer_barcode", "").strip()

        # Save the new customer
        new_customer = Customer(
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
            customer_barcode=customer_barcode,
        )
        new_customer.save()
        messages.success(request, "Customer added successfully!")

        # Redirect to the customer list page after adding
        return redirect(Customers)

    return render(request, "Customers/addform.html")

def editCustomer(request, id):
    cData = Customer.objects.get(id=int(id))  # Get customer data by ID
    if request.method == "GET":
        context = {
            "cData": cData
        }
        return render(request, "Customers/Custedit.html", context)
    else:
        # Collecting updated data from form
        name = request.POST.get("name").strip()
        mobile_no = request.POST.get("mobile_no").strip()
        email = request.POST.get("email").strip()
        gst_no = request.POST.get("gst_no").strip()
        pan_no = request.POST.get("pan_no").strip()
        opening_balance = request.POST.get("opening_balance")
        group_type = request.POST.get("group_type")
        billing_address = request.POST.get("billing_address")
        shipping_address = request.POST.get("shipping_address")
        city = request.POST.get("city")
        credit_limit = request.POST.get("credit_limit")
        credit_period = request.POST.get("credit_period")
        customer_barcode = request.POST.get("customer_barcode")
        
        # Updating customer data
        cData.name = name
        cData.mobile_no = mobile_no
        cData.email = email
        cData.gst_no = gst_no
        cData.pan_no = pan_no
        cData.opening_balance = opening_balance
        cData.group_type = group_type
        cData.billing_address = billing_address
        cData.shipping_address = shipping_address
        cData.city = city
        cData.credit_limit = credit_limit
        cData.credit_period = credit_period
        cData.customer_barcode = customer_barcode
        
        cData.save()
        messages.success(request, "Customer details updated successfully!")
        return redirect(Customers)

def deleteCustomer(request, id):
    try:
        cData = Customer.objects.get(id=int(id))  # Fetch customer by ID
        cData.delete()  # Delete the customer
        messages.success(request, "Customer deleted successfully!")
    except Customer.DoesNotExist:
        messages.error(request, "Customer not found.")
    return redirect(Customers)  # Redirect to customer list
