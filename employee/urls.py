from django.urls import path
from rest_framework.routers import DefaultRouter
from employee.views import EmployeesPage, DevicesPage, EmployeesViewSet, DevicesViewSet

router = DefaultRouter()
router.register('api/Employees', EmployeesViewSet)
router.register('api/Devices', DevicesViewSet)

urlpatterns = [
    path('employees', EmployeesPage, name='employee'),
    path('devices', DevicesPage, name='device'),
]

urlpatterns += router.urls
