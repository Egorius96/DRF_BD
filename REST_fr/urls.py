from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from REST_fr.views import ModelViewSetclass, ListAPIViewclass, RetrieveAPIViewclass,\
    CreateAPIViewclass, UpdateAPIViewclass, DestroyAPIViewclass

router = SimpleRouter()
router.register('api/ModelViewSet', ModelViewSetclass)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/list/', ListAPIViewclass.as_view()),
    path('api/create/', CreateAPIViewclass.as_view()),
    path('api/detail/<int:pk>', RetrieveAPIViewclass.as_view()),
    path('api/update/<int:pk>', UpdateAPIViewclass.as_view()),
    path('api/delete/<int:pk>', DestroyAPIViewclass.as_view()),

]

urlpatterns += router.urls
