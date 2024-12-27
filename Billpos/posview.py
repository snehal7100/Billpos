from django.shortcuts import render

def posdashboard(request):
    # Render the POS index template
    return render(request, "Pos/posindex.html")
