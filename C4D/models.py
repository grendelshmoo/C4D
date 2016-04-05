from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=200)
    airport_code = models.CharField(max_length=3)

class LandRecord(models.Model):
    grantor = models.CharField(max_length=64)
    grantee = models.CharField(max_length=64)
