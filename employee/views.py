from django.shortcuts import render
from employee.models import EmployeeModel
from rest_framework import viewsets
from employee.serializers import DefaultViewSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = DefaultViewSerializer


def index(request):
    return render(request, 'employee/index.html')


def EmployeePage(request):
    employee = EmployeeModel.objects.all()
    return render(request, 'employee/employee.html', {'employee': employee})
