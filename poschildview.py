import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from poschild.models import PosChild
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt  # Only needed if you are using AJAX
def save_billchild(request):
    if request.method == 'POST':
        pos_master = request.POST.get('pos_master')
        item_name = request.POST.get('item_name')
        qty = request.POST.get('qty')
        mrp = request.POST.get('mrp')
        sale_price = request.POST.get('sale_price')
        total = request.POST.get('total')
       
        return JsonResponse({'message': 'Bill saved successfully!'}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)

   


def bill_report(request):
    poschild_data = PosChild.objects.all()  # Fetch data
    return render(request, 'Report/billreport.html', {'poschild_data': poschild_data})

