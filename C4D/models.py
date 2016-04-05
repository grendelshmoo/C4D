from django.db import models

class Office(models.Model):
    name = models.CharField(max_length=200)
    airport_code = models.CharField(max_length=3)

