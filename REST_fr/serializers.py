from rest_framework.serializers import ModelSerializer
from REST_fr.models import Book


class DefaultViewSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name']


class DetailViewSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'description']
