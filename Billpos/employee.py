from django.shortcuts import render, redirect
from Employee.models import Employee
from django.contrib import messages


def emp(request):
    EmployeeData = Employee.objects.all()
    data = {
        "EmployeeData": EmployeeData
    }
    return render(request, 'Employee/index.html', data)


def employeeview(request, id):
    EmployeeData = Employee.objects.all()
    data = {
        "EmployeeData": EmployeeData,
        "id": int(id),
    }
    return render(request, 'Employee/view.html', data)


def editemployee(request, id):
    EmployeeData = Employee.objects.get(id=int(id))  # Get customer data by ID
    if request.method == "GET":
        context = {
            "EmployeeData": EmployeeData
        }
        return render(request, "Employee/edit.html", context)
    else:
        # Collecting updated data from form
        membername = request.POST.get("membername").strip()
        mobno = request.POST.get("mobno").strip()
        emobno = request.POST.get("emobno").strip()
        emaileadd = request.POST.get("emaileadd").strip()
        password = request.POST.get("password").strip()
        salary = request.POST.get("salary").strip()
        datejoining = request.POST.get("datejoining")
        department = request.POST.get("department")
        role = request.POST.get("role")
        lastexperience = request.POST.get("lastexperience")
        lastworkcom = request.POST.get("lastworkcom")
        lastcomsalary = request.POST.get("lastcomsalary")
        adharnum = request.POST.get("adharnum")
        pannum = request.POST.get("pannum")
        userupi = request.POST.get("userupi")
        address = request.POST.get("address")
        adharimg = request.POST.get("adharimg")
        panimg = request.FILES.get("panimg")
        proimg = request.FILES.get("proimg")
        qrimg = request.FILES.get("qrimg")

        EmployeeData.membername = membername
        EmployeeData.mobno = mobno
        EmployeeData.emobno = emobno
        EmployeeData.emaileadd = emaileadd
        EmployeeData.password = password
        EmployeeData.salary = salary
        EmployeeData.datejoining = datejoining
        EmployeeData.department = department
        EmployeeData.role = role
        EmployeeData.lastexperience = lastexperience
        EmployeeData.lastworkcom = lastworkcom
        EmployeeData.lastcomsalary = lastcomsalary
        EmployeeData.adharnum = adharnum
        EmployeeData.pannum = pannum
        EmployeeData.userupi = userupi
        EmployeeData.address = address
        EmployeeData.adharimg = adharimg
        EmployeeData.panimg = panimg
        EmployeeData.proimg = proimg
        EmployeeData.qrimg = qrimg

        EmployeeData.save()
        messages.success(request, "Employee details updated successfully!")
        return redirect(emp)


def deleteemployee(request, id):
    EmployeeData = Employee.objects.get(id=int(id))
    EmployeeData.delete()
    messages.success(request, "Employee deleted successfully!")
    return redirect(emp)
def Addemployee(request):
    if request.method == "GET":
        return render(request, "Employee/index.html")
    else:
        membername = request.POST.get("membername").strip()
        mobno = request.POST.get("mobno").strip()
        emobno = request.POST.get("emobno").strip()
        emaileadd = request.POST.get("emaileadd").strip()
        password = request.POST.get("password").strip()
        salary = request.POST.get("salary").strip()
        datejoining = request.POST.get("datejoining")
        department = request.POST.get("department")
        role = request.POST.get("role")
        lastexperience = request.POST.get("lastexperience")
        lastworkcom = request.POST.get("lastworkcom")
        lastcomsalary = request.POST.get("lastcomsalary")
        adharnum = request.POST.get("adharnum")
        pannum = request.POST.get("pannum")
        userupi = request.POST.get("userupi")
        address = request.POST.get("address")
        adharimg = request.POST.get("adharimg")
        panimg = request.FILES.get("panimg")
        proimg = request.FILES.get("proimg")
        qrimg = request.FILES.get("qrimg")

        
        saveData = Employee(
        membername = membername,
        mobno = mobno,
        emobno = emobno,
        emaileadd = emaileadd,
        password = password,
        salary = salary,
        datejoining = datejoining,
        department = department,
        role = role,
        lastexperience = lastexperience,
        lastworkcom = lastworkcom,
        lastcomsalary = lastcomsalary,
        adharnum = adharnum,
        pannum = pannum,
        userupi = userupi,
        address = address,
        adharimg = adharimg,
        panimg = panimg,
        proimg = proimg,
        qrimg = qrimg,
        )
        saveData.save()
        messages.success(request, "Employee added successfully!")
        return redirect(emp)
