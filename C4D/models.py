from django.db import models

class TitleCompany(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Municipality(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Condominium(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

# Change to choice field?
class Island(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length=200)
    airport_code = models.CharField(max_length=3)

    def __unicode__(self):
        return "%s (%s) " % (self.name, self.airport_code)

class Property(models.Model):
    legal_description = models.CharField(max_length=256, blank=True, null=True)
    lot = models.CharField(max_length=64, blank=True, null=True)
    block = models.CharField(max_length=32, blank=True, null=True)
    unit = models.CharField(max_length=32, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    phase = models.CharField(max_length=32, blank=True, null=True)
    tract = models.IntegerField()
    increment = models.PositiveSmallIntegerField()
    lot_sf = models.FloatField(blank=True, null=True)
    building_sf = models.FloatField(blank=True, null=True)
    map_document = models.IntegerField()
    building_type = models.CharField(max_length=32, blank=True, null=True)
    year_built = models.PositiveSmallIntegerField(blank=True, null=True)
    construction_type  = models.CharField(max_length=32, blank=True, null=True)
    building_condition = models.CharField(max_length=32, blank=True, null=True)
    island = models.ForeignKey(Island, blank=False, null=False)
    municipality = models.ForeignKey(Municipality, blank=True, null=True)
    condominium = models.ForeignKey(Condominium, blank=True, null=True)

class LandRecord(models.Model):
    office = models.ForeignKey(Office, null=False)
    property = models.ForeignKey(Property, null=False)
    document_date = models.DateField(blank=True, null=True)
    recording_date = models.DateField(blank=True, null=True)
    document_type = models.CharField(max_length=128, blank=True, null=True)
    title_company = models.ForeignKey(TitleCompany, blank=True, null=True)
    instrument_number = models.CharField(max_length=32, blank=True, null=True)
    fy_number = models.CharField(max_length=64, blank=True, null=True)
    cnmi_file_numer = models.CharField(max_length=32, blank=True, null=True)
    lcdn = models.IntegerField(blank=True, null=True)
    book = models.PositiveSmallIntegerField(blank=True, null=True)
    page = models.PositiveSmallIntegerField(blank=True, null=True)
    #properties = models.ManyToManyField('Property', blank=True, null=True)

class Transaction(models.Model):
    # One to one?
    record = models.ForeignKey(LandRecord, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    recording_fees = models.FloatField(default=0.0)
    land_tax = models.FloatField(default=0.0)
    building_tax = models.FloatField(default=0.0)
    land_appraised_value = models.FloatField(default=0.0)
    building_appraised_value = models.FloatField(default=0.0)
