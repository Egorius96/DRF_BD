from dataclasses import fields

from rest_framework.serializers import ModelSerializer
from employee.models import Employee, Device


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class DevicesSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'