from django.urls import path
from rest_framework.routers import DefaultRouter
from employee.views import EmployeePage, EmployeeViewSet

router = DefaultRouter()
router.register('api', EmployeeViewSet)

urlpatterns = [
    path('', EmployeePage, name='employee'),
]

urlpatterns += router.urls
