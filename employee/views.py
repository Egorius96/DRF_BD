from django.shortcuts import render
from employee.models import Employee, Device
from rest_framework import viewsets
from employee.serializers import EmployeesSerializer, DevicesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer


class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DevicesSerializer


def index(request):
    return render(request, 'employee/index.html')


def EmployeesPage(request):
    employee = Employee.objects.all()
    device = Device.objects.all()
    return render(request, 'employee/employees.html', {'employee': employee, 'device': device})

def DevicesPage(request):
    employee = Employee.objects.all()
    device = Device.objects.all()
    return render(request, 'employee/devices.html', {'employee': employee, 'device': device})
