from django.shortcuts import render, redirect, get_object_or_404
from Taxes.models import Taxs
from django.contrib import messages

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
        return redirect('tax-view', id=id)  # Redirect to the updated tax record detail
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
        sr_no = request.POST.get("sr_no").strip()
        taxname = request.POST.get("taxname").strip()
        taxpercentage = request.POST.get("taxpercentage").strip()

        # Server-side validation
        if not sr_no or not taxname or not taxpercentage:
            messages.error(request, "All fields are required.")
            return render(request, "Tax/Taxaddform.html", {
                'sr_no': sr_no,
                'taxname': taxname,
                'taxpercentage': taxpercentage
            })

        # Save the new tax record if validation passes
        newTax = Taxs(
            sr_no=sr_no,
            taxname=taxname,
            taxpercentage=taxpercentage
        )
        newTax.save()
        messages.success(request, "Tax record added successfully.")
        return redirect('Tax-list')  # Redirect to the list page

    # Render the form for GET requests
    return render(request, "Tax/Taxaddform.html")