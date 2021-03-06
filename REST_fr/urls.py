from django.contrib import admin
from django.urls import path, include
from employee.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('info/', include('employee.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
