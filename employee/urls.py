from django.urls import path
from rest_framework.routers import DefaultRouter
from employee.views import employees_page, devices_page, EmployeesViewSet, DevicesViewSet

router = DefaultRouter()
router.register('api/Employees', EmployeesViewSet)
router.register('api/Devices', DevicesViewSet)

urlpatterns = [
    path('employees', employees_page, name='employee'),
    path('devices', devices_page, name='device'),
]

urlpatterns += router.urls
