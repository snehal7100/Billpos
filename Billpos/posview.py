from django.shortcuts import render
from Customer.models import Customer
from Product.models import ProductModel
from payment.models import Payment 
# from Brand.models import BrandForm as Brand
# from Taxes.models import Taxs as Tax
# from category.models import Category  

def posdashboard(request):
    # Fetch customer, product, and payment data
    cData = Customer.objects.all()  # Fetch all customer records
    pData = ProductModel.objects.all()  # Fetch all product records
    paymentData = Payment.objects.all()
    # brand_query = "SELECT * FROM tbl_brand"
    # bData = Brand.objects.raw(brand_query)
    # taxes_query = "SELECT * FROM tbl_taxes"
    # taxData = Tax.objects.raw(taxes_query)
    # category_query = "SELECT * FROM tbl_category"
    # categoryData = Category.objects.raw(category_query)
    
      # Fetch all payment terms

    return render(request, "Pos/posindex.html", {
        "customerData": cData,
        "productData": pData,
        "paymentData": paymentData,
        # "bData": bData,  # Brand data for dropdown
        # "taxData": taxData,  # Tax data for dropdown
        # "categoryData": categoryData,  # Category data for dropdown

    })
