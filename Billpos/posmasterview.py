import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from posmaster.models import PosMaster
from poschild.models import PosChild
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Only needed if you are using AJAX
def save_bill(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        credit_amt = request.POST.get('credit_amt')
        payment_term = request.POST.get('payment_term')
        total = request.POST.get('total')
        bill_date = request.POST.get('bill_date')

        # Create a new PosMaster entry
        temp = PosMaster.objects.create(
            customer_name=customer_name,
            mobile_no=mobile_no,
            address=address,
            credit_amt=credit_amt,
            payment_term=payment_term,
            total=total,
            bill_date=bill_date,
        )

        item_name = request.POST.get('item_name')  
        qty = request.POST.get('qty')
        mrp = request.POST.get('mrp')
        sale_price = request.POST.get('sale_price')
        item_total = request.POST.get('item_total')  

        items = json.loads(request.POST.get('items'))  # Parse JSON list of items
        for item in items:
            PosChild.objects.create(
            pos_master=temp,
            item_name=item['item_name'],
            qty=item['qty'],
            mrp=item['mrp'],
            sale_price=item['sale_price'],
            total=item['total'],
        )


        return JsonResponse({'message': 'Bill saved successfully!'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)
