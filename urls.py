"""
URL configuration for Billpos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Billpos import settings  
from django.conf.urls.static import static  


from django.contrib import admin
from django.urls import path
from Billpos import view
from Billpos import categoryview

from Billpos import brandview
from Billpos import productview


from Billpos import Taxview

from Billpos import loginvalid

from Billpos import customerview
from Billpos import Dashboardview

from Billpos import supplierview
from Billpos import posview

from Billpos import employee
from Billpos import Paymentview



from Billpos import rewardsview
from Billpos import barcodeview
from Billpos import posmasterview
from Billpos import poschildview
# from Billpos import poschildview
from Billpos import billlistview


urlpatterns = [ 
    path('save-bill/', posmasterview.save_bill, name='save_bill'),

    #  path('save_billchild/', poschildview.save_billchild, name='save_billchild'),
    path('customer-report/',posmasterview.customer_report),

    path('BillList/', billlistview.BillList, name='bill_list'),  # List page
    path('bill_view/<int:id>/', billlistview.BillView, name='bill_view'), 
    path('bill-report/', poschildview.bill_report),


    path('dashboard/', Dashboardview.dashboard),
    path('pos/', posview.posdashboard),
    path('barcode-print/', barcodeview.Barcodes),


    path('category-list/',categoryview.category),
    path('category-add/',categoryview.addcategory),
    path('category-view/<id>',categoryview.categoryview),
    path('category-edit/<id>',categoryview.editcategory),
    path('category-delete/<id>',categoryview.delete),


    path('admin/', admin.site.urls), 
    path('', view.Login),  
    path('valid/', loginvalid.login_view), 
    path('index/', Dashboardview.dashboard), 

    path('brand-list/', brandview.Brands),
    path('brand-edit/<id>', brandview.editBrand),
    path('brand-delete/<id>', brandview.delete),
    path('brand-add/', brandview.AddBrand),


    path('tax-list/', Taxview.TaxList),  
    path('tax-view/<id>/', Taxview.TaxView),  
    path('tax-edit/<id>/', Taxview.editTax),  
    path('tax-delete/<id>/', Taxview.deleteTax),  
    path('tax-add/', Taxview.addTax),  


    path('customer-list/', customerview.Customers),
    path('customer-view/<int:id>', customerview.editCustomer),
    path('customer-edit/<int:id>', customerview.editCustomer),
    path('customer-delete/<int:id>', customerview.deleteCustomer),  # Correctly capture integer ID
    path('customer-add/', customerview.AddCustomer),  

    path('product-list/', productview.Products),
    path('product-edit/<id>', productview.EditProduct),
    path('product-delete/<id>', productview.delete),
    path('product-add/', productview.AddProduct),

    path('supplier-list/', supplierview.SuppliersList),  
    path('supplier-view/<id>/', supplierview.editSupplier), 
    path('supplier-edit/<id>/', supplierview.editSupplier),  
    path('supplier-delete/<id>/', supplierview.deleteSupplier), 
    path('supplier-add/', supplierview.AddSupplier),



    path('Employee-list/', employee.emp),  
    path('Employee-view/<id>/', employee.employeeview), 
    path('Employee-edit/<id>/', employee.editemployee),  
    path('Employee-delete/<id>/', employee.deleteemployee), 
    path('Employee-add/', employee.Addemployee),  




path('rewards-list/', rewardsview.Rewards),
path('rewards-add/', rewardsview.AddRewards),
path('rewards-edit/<id>/', rewardsview.editRewards),  
path('rewards-delete/<id>', rewardsview.delete),





    path('Payment-list/', Paymentview.payments),
    path('Payment-edit/<id>', Paymentview.editpayment),
    path('Payment-delete/<id>', Paymentview.delete),
    path('Payment-add/', Paymentview.AddPayment),




    
   



]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  