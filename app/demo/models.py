from django.db import models
from django.contrib.postgres.fields import ArrayField


class Demo(models.Model):
    name = models.CharField(max_length=30)
    arrf_1d = ArrayField(models.CharField(max_length=3, blank=True), null=True)
    arrf_2d = ArrayField(ArrayField(models.IntegerField()), size=2, null=True)
    jfield = models.JSONField(default=dict, null=True)


class Product(models.Model):
    name = models.CharField(max_length=20)
    name_idx = models.CharField(max_length=20)
    attributes = models.JSONField()
    attributes_idx = models.JSONField()