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
        taxname = request.POST.get("taxname", "").strip()
        taxpercentage = request.POST.get("taxpercentage", "").strip()

        # Server-side validation for empty fields
        if not taxname or not taxpercentage:
            if not taxname:
                messages.error(request, "")
            if not taxpercentage:
                messages.error(request, "")

            # Re-render the form with the current data if validation fails
            return render(request, "Tax/Taxedit.html", {
                "taxData": taxData
            })

        # Update the tax record
        taxData.taxname = taxname
        taxData.taxpercentage = taxpercentage
        taxData.save()
       
        return redirect(TaxList)
 # Redirect to the updated tax record detail

    context = {
        "taxData": taxData
    }
    return render(request, "Tax/Taxedit.html", context)


# View to delete a tax record
def deleteTax(request, id):
    taxData = get_object_or_404(Taxs, id=id)
    taxData.delete()
    messages.success(request, "Tax record deleted successfully.")
    return redirect(TaxList)  # Correct redirect to tax-list


# View to add a new tax record
def addTax(request):
    if request.method == "POST":
        # Getting form data
        sr_no = request.POST.get("sr_no", "").strip()
        taxname = request.POST.get("taxname", "").strip()
        taxpercentage = request.POST.get("taxpercentage", "").strip()

        # Server-side validation for empty fields and invalid inputs
        errors = []
        if not sr_no:
            errors.append("SR No is required.")
        if not taxname:
            errors.append("Tax Name is required.")
        if not taxpercentage:
            errors.append("Tax Percentage is required.")
        elif not taxpercentage.isdigit() or not (0 <= float(taxpercentage) <= 100):
            errors.append("Tax Percentage must be a number between 0 and 100.")

        # Check for duplicate SR No or Tax Name
        if Taxs.objects.filter(sr_no=sr_no).exists():
            errors.append("SR No must be unique.")
        if Taxs.objects.filter(taxname__iexact=taxname).exists():
            errors.append("Duplicate entry not allowed! Tax Name already exists.")

        # If there are any validation errors, show them
        if errors:
            for error in errors:
                messages.error(request, error)

            # Re-render the form with previously entered data
            return render(request, "Tax/Taxaddform.html", {
                "sr_no": sr_no,
                "taxname": taxname,
                "taxpercentage": taxpercentage
            })

        # Save the new tax record if validation passes
        new_tax = Taxs(
            sr_no=sr_no,
            taxname=taxname,
            taxpercentage=taxpercentage
        )
        new_tax.save()
        messages.success(request, "Tax record added successfully!")
        return redirect(TaxList)  # Redirect to the tax list page

    # Render the form for GET requests
    return render(request, TaxList)
