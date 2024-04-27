from django.contrib.contenttypes.fields import (
    GenericRelation, GenericForeignKey
)
from django.contrib.contenttypes.models import ContentType
from django.db import models



class Image(models.Model):
    image = models.CharField(max_length=32, null=True) # path
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = "Image"
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


class Property(models.Model):
    name = models.CharField(max_length=32)
    images = GenericRelation(Image)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Property"


class User(models.Model):
    name = models.CharField(max_length=32)
    images = GenericRelation(Image)

    class Meta:
        verbose_name = "Property"
