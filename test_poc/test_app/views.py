from django.shortcuts import render
from django.shortcuts import HttpResponse
from test_app.models import Employee
# Create your views here.

def welcome(request):
    sample_msg = "welcome to Django"
    return HttpResponse(sample_msg)

def home(request):
    return render(request, 'test_app/home.html')

def insertdata(request):
    name = request.POST.get("name")
    id = request.POST.get("id")
    Employee_object = Employee(employee_name=name, employee_id=id)
    Employee_object.save()
    employee_details = get_details(request)
    return render(request, 'test_app/display.html', {"details" : employee_details})

def display_details(request):
    employee_details = get_details(request)
    return render(request, 'test_app/display.html', {"details" : employee_details})

def get_details(request):
    results = Employee.objects.all()
    employee_details = {}
    for item in results:
        employee_details[item.employee_name] = item.employee_id
    return employee_details