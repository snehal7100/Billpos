from django.shortcuts import render, redirect
from Taxes.models import Taxs 

# View to display all tax records
def TaxList(request):
    taxData = Taxs.objects.all()  
    context = {
        "taxData": taxData
    }
    return render(request, "Tax/Taxindex.html", context)  


# def TaxView(request, id):
#     taxData = Taxs.objects.filter(id=id).first()  
#     context = {
#         "taxData": taxData
#     }
#     return render(request, "Tax/view.html", context)  
