from django.shortcuts import render, get_object_or_404
from posmaster.models import PosMaster  # Or wherever your model is
from Customer.models import Customer  # If you use Customer model for the bill info

# Bill list view
def BillList(request):
    posmaster_data = PosMaster.objects.all()  # Fetch all bill data
    return render(request, 'Pos/posBillList.html', {'posmaster_data': posmaster_data})

# Bill detail view
def BillView(request, id):
    posmaster_data = PosMaster.objects.all()  # Or fetch based on specific criteria if needed
    return render(request, "Pos/posBillListView.html", {'posmaster_data': posmaster_data, 'id': id})    