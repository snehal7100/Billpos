from django.shortcuts import render
def Login(request):
    return render(request,"Component/index.html")

def Index(request):
    return render(request,"index.html")