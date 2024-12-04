from django.shortcuts import render, redirect, get_object_or_404
from Taxes.models import Taxs

# View to display all tax records
def TaxList(request):
    taxData = Taxs.objects.all()
    context = {
        "taxData": taxData
    }
    return render(request, "Tax/Taxindex.html", context)


# View to display a single tax record
def TaxView(request, id):
    taxData = get_object_or_404(Taxs, id=id)  # Handle 404 if ID is not found
    context = {
        "taxData": taxData
    }
    return render(request, "Tax/Taxview.html", context)


# View to edit a tax record
def editTax(request, id):
    taxData = get_object_or_404(Taxs, id=id)
    if request.method == "POST":
        taxData.taxname = request.POST.get("taxname", taxData.taxname)
        taxData.taxpercentage = request.POST.get("taxpercentage", taxData.taxpercentage)
        taxData.save()
        return redirect(TaxList)
    else:
        context = {
            "taxData": taxData
        }
        return render(request, "Tax/Taxedit.html", context)


# View to delete a tax record
def deleteTax(request, id):
    taxData = get_object_or_404(Taxs, id=id)
    taxData.delete()
    return redirect(TaxList)


# View to add a new tax record
def addTax(request):
    if request.method == "POST":
        sr_no = request.POST.get("sr_no")
        taxname = request.POST.get("taxname")
        taxpercentage = request.POST.get("taxpercentage")

        # Save the new tax record
        newTax = Taxs(
            sr_no=sr_no,
            taxname=taxname,
            taxpercentage=taxpercentage
        )
        newTax.save()
        return redirect(TaxList)
    else:
        return render(request, "Tax/Taxaddform.html")
