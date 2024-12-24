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

from Billpos import supplierview



urlpatterns = [

    # path('profile-view/<id>', Adminview.view_profile),

    # path('profile/edit/', Adminview.edit_profile),
    # path('profile/logout/', Adminview.logout_user),


    path('category-list/',categoryview.category),
    path('category-add/',categoryview.addcategory),
    path('category-view/<id>',categoryview.categoryview),
    path('category-edit/<id>',categoryview.editcategory),
    path('category-delete/<id>',categoryview.delete),


    path('admin/', admin.site.urls), 
    path('', view.Login),  
    path('valid/', loginvalid.login_view), 
    path('index/', view.Index), 

   
 
    
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
    path('customer-view/<id>/', customerview.editCustomer), 
    path('customer-edit/<id>/', customerview.editCustomer),  
    path('customer-delete/<id>/', customerview.deleteCustomer), 
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




]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  