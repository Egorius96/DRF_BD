from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
