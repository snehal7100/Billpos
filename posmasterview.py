import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from posmaster.models import PosMaster
from poschild.models import PosChild
from django.views.decorators.csrf import csrf_exempt



def posbills_list(request):
    pos_bills = PosMaster.objects.all()
    return render(request, 'posindex.html', {'pos_bills': pos_bills})



@csrf_exempt  # Only needed if you are using AJAX
def save_bill(request):
    if request.method == "POST":
        # Extracting the data from the request
        customer_name = request.POST.get('customer_name')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        credit_amt = request.POST.get('credit_amt')
        payment_term = request.POST.get('payment_term')
        total = request.POST.get('total')
        bill_date = request.POST.get('bill_date')
        items = json.loads(request.POST.get('items'))  # PosChild items data

        # Create a new PosMaster record
        pos_master = PosMaster.objects.create(
            customer_name=customer_name,
            mobile_no=mobile_no,
            address=address,
            credit_amt=credit_amt,
            payment_term=payment_term,
            total=total,
            bill_date=bill_date
        )


        
        items = json.loads(request.POST.get('items'))
        # return print( "item: s",items)  # Parse JSON list of items

        # Create PosChild records for each product

        for item in items:
            PosChild.objects.create(
                pos_master=pos_master,  # Link to PosMaster
                item_name=item['item_name'],
                qty=item['qty'],
                mrp=item['mrp'],
                sale_price=item['sale_price'],
                total=item['total']
            )

        # Return a response (success message)
        return JsonResponse({"message": "Bill saved successfully!"})

    return JsonResponse({"error": "Invalid request"}, status=400)

def customer_report(request):
    posmaster_data = PosMaster.objects.all()  # Fetch data
    return render(request, 'Report/custreport.html', {'posmaster_data': posmaster_data})