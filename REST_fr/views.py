from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from REST_fr.models import Book
from REST_fr.serializers import DetailViewSerializer, DefaultViewSerializer


# How to №1
class ModelViewSetclass(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = DefaultViewSerializer


# How to №2
class ListAPIViewclass(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = DefaultViewSerializer


class RetrieveAPIViewclass(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailViewSerializer


class CreateAPIViewclass(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailViewSerializer


class UpdateAPIViewclass(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailViewSerializer


class DestroyAPIViewclass(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailViewSerializer
