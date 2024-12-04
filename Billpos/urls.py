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
<<<<<<< HEAD
from Billpos import categoryview

=======
from Billpos import brandview
<<<<<<< HEAD
>>>>>>> f3dc596972694f5ff1271d30b9e41b8683805be5

=======
from Billpos import Taxview
>>>>>>> 6d758955df8cc3a114622fc220efee0abb354f0d
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Login),
    path('index/', view.Index),

<<<<<<< HEAD

    path('category-list/',categoryview.category),
    path('category-add/',categoryview.addcategory),
    path('category-view/<id>',categoryview.categoryview),
    path('category-edit/<id>',categoryview.editcategory),
    path('category-delete/<id>',categoryview.delete),
=======
   
    path('brand-list/', brandview.Brands),
    path('brand-view/<id>', brandview.BrandView),
    path('brand-edit/<id>', brandview.editBrand),
    path('brand-delete/<id>', brandview.delete),
    path('brand-add/', brandview.AddBrand),
    

    path('Tax-list/', Taxview.TaxList), 

>>>>>>> f3dc596972694f5ff1271d30b9e41b8683805be5

]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  