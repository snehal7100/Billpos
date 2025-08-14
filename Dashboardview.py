# views.py
from django.shortcuts import render
from Supplier.models import Suppliers
from Customer.models import Customer
from Product.models import ProductModel
from posmaster.models import PosMaster

def dashboard(request):
    # Fetch counts from the database
    total_products = ProductModel.objects.count()
    total_customers = Customer.objects.count()
    total_suppliers = Suppliers.objects.count()
    total_bills=PosMaster.objects.count()

    # Pass counts to the template
    context = {
        "total_products": total_products,
        "total_customers": total_customers,
        "total_suppliers": total_suppliers,
        "total_bills":total_bills,
    }
    return render(request, "Component/dashboard.html", context)

