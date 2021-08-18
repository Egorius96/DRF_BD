from rest_framework.serializers import ModelSerializer
from employee.models import EmployeeModel


class DefaultViewSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'device', 'configuration', 'price', 'paid_by', 'used_by', 'image', 'team', 'comment', 'item_number']

