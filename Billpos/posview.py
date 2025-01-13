from django.shortcuts import render
from Customer.models import Customer
from Product.models import ProductModel
from payment.models import Payment  # Import the Payment model

def posdashboard(request):
    # Fetch customer, product, and payment data
    cData = Customer.objects.all()  # Fetch all customer records
    pData = ProductModel.objects.all()  # Fetch all product records
    paymentData = Payment.objects.all()  # Fetch all payment terms

    return render(request, "Pos/posindex.html", {
        "customerData": cData,
        "productData": pData,
        "paymentData": paymentData  # Pass payment terms to the template
    })
