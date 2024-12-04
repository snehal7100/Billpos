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
from Billpos import brandview
from Billpos import Taxview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Login),
    path('valid/',view.login_view),
    path('index/', view.Index),

   
    path('brand-list/', brandview.Brands),
    path('brand-view/<id>', brandview.BrandView),
    path('brand-edit/<id>', brandview.editBrand),
    path('brand-delete/<id>', brandview.delete),
    path('brand-add/', brandview.AddBrand),
    

    path('Tax-list/', Taxview.TaxList),
    path('tax-view/<id>', Taxview.TaxView),
    path('tax-edit/<id>', Taxview.editTax),
    path('tax-delete/<id>', Taxview.deleteTax),
    path('tax-add/', Taxview.addTax),


]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  