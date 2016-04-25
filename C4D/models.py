from django.db import models

class TitleCompany(models.Model):
    name = models.CharField(max_length=256)

class Municipality(models.Model):
    name = models.CharField(max_length=256)

class Condominium(models.Model):
    name = models.CharField(max_length=256)

class Island(models.Model):
    name = models.CharField(max_length=256)

class Office(models.Model):
    name = models.CharField(max_length=200)
    airport_code = models.CharField(max_length=3)

class LandRecord(models.Model):
    office = models.ForeignKey(Office, null=False)
    document_date = models.DateField(blank=True, null=True)
    recording_date = models.DateField(blank=True, null=True)
    document_type = models.CharField(max_length=128, blank=True, null=True)
    title_company = models.ForeignKey(TitleCompany, blank=True, null=True)
    instrument_number = models.CharField(max_length=32, blank=True, null=True)
    fy_number = models.CharField(max_length=64, blank=True, null=True)
    land_registry = models.CharField(max_length=32, blank=True, null=True)
    lcdn = models.IntegerField(default=0)
    book = models.PositiveSmallIntegerField(default=0)
    page = models.PositiveSmallIntegerField(default=0)
    properties = models.ManyToManyField('Property')

class Property(models.Model):
    legal_description = models.CharField(max_length=256, null=False)
    lot = models.CharField(max_length=64, blank=True, null=True)
    block = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    area = models.FloatField(default=0.0)
    phase = models.CharField(max_length=32, blank=True, null=True)
    tract = models.IntegerField(default=0)
    increment = models.PositiveSmallIntegerField(default=0)
    lot_sf = models.FloatField(default=0.0)
    building_sf = models.FloatField(default=0.0)
    map_document = models.IntegerField(default=0)
    building_type = models.CharField(max_length=32, blank=True, null=True)
    year_built = models.PositiveSmallIntegerField(default=0)
    construction_type  = models.CharField(max_length=32, blank=True, null=True)
    building_condition = models.CharField(max_length=32, blank=True, null=True)
    municipality = models.ForeignKey(Municipality, blank=True, null=True)
    condominium = models.ForeignKey(Condominium, blank=True, null=True)
    island = models.ForeignKey(Island, blank=True, null=True)

class Transaction(models.Model):
    record = models.ForeignKey(LandRecord, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    recording_fees = models.FloatField(default=0.0)
    land_tax = models.FloatField(default=0.0)
    building_tax = models.FloatField(default=0.0)
    land_appraised_value = models.FloatField(default=0.0)
    building_appraised_value = models.FloatField(default=0.0)
