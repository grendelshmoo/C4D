from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ImportLog(models.Model):
    imported_by = models.ForeignKey(User, blank=True, null=True, related_name="+")
    start_ts = models.DateTimeField(auto_now_add=True)
    end_ts = models.DateTimeField(null=True, blank=True)
    file_name = models.CharField(max_length=256)

    def mark_end(self):
        self.end_ts = timezone.now()
        self.save()

    def __unicode__(self):
        return self.file_name


class RawLandRecord(models.Model):
    office = models.CharField(max_length=3)
    document_date = models.DateField(blank=True, null=True)
    recording_date = models.DateField(blank=True, null=True)
    document_type = models.CharField(max_length=128, blank=True, null=True)
    grantor = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    grantee = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    title_company = models.CharField(max_length=512, blank=True, null=True)
    legal_description = models.CharField(max_length=1024, blank=True, null=True, db_index=True)
    lot = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    block = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    tract = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    unit = models.CharField(max_length=128, blank=True, null=True)
    area = models.CharField(max_length=128, blank=True, null=True)
    phase = models.CharField(max_length=128, blank=True, null=True)
    increment = models.CharField(max_length=128, blank=True, null=True)
    lot_sf = models.CharField(max_length=128, blank=True, null=True)
    building_sf = models.CharField(max_length=128, blank=True, null=True)
    map_document = models.CharField(max_length=128, blank=True, null=True)
    building_type = models.CharField(max_length=128, blank=True, null=True)
    year_built = models.CharField(max_length=128, blank=True, null=True)
    construction_type  = models.CharField(max_length=128, blank=True, null=True)
    building_condition = models.CharField(max_length=128, blank=True, null=True)
    island = models.CharField(max_length=256, blank=True, null=True)
    municipality = models.CharField(max_length=512, blank=True, null=True)
    condominium = models.CharField(max_length=512, blank=True, null=True)
    instrument_number = models.CharField(max_length=128, blank=True, null=True)
    fy_number = models.CharField(max_length=128, blank=True, null=True)
    cnmi_file_number = models.CharField(max_length=128, blank=True, null=True)
    lcdn = models.CharField(max_length=128, blank=True, null=True)
    book = models.CharField(max_length=128, blank=True, null=True)
    page = models.CharField(max_length=128, blank=True, null=True)
    amount = models.CharField(max_length=128, blank=True, null=True)
    recording_fees = models.CharField(max_length=128, blank=True, null=True)
    land_tax = models.CharField(max_length=128, blank=True, null=True)
    building_tax = models.CharField(max_length=128, blank=True, null=True)
    land_appraised_value = models.CharField(max_length=128, blank=True, null=True)
    building_appraised_value = models.CharField(max_length=128, blank=True, null=True)
    remarks = models.CharField(max_length=1024, blank=True, null=True)
    import_log = models.ForeignKey(ImportLog, blank=True, null=True, db_index=True)

    def __unicode__(self):
        description = ""
        if self.legal_description:
            description = self.legal_description
        else:
            if self.lot:
                description += "lot: " + self.lot
            if self.block:
                description += " block: " + self.block
            if self.tract:
                description += " tract: " + self.tract
        if not description:
            description = "ID: " + str(self.id)
        return description.strip()


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


class Plot(models.Model):
    legal_description = models.CharField(max_length=256, blank=True, null=True)
    lot = models.CharField(max_length=64, blank=True, null=True)
    block = models.CharField(max_length=32, blank=True, null=True)
    tract = models.IntegerField()
    unit = models.CharField(max_length=32, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    phase = models.CharField(max_length=32, blank=True, null=True)
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
    plot = models.ForeignKey(Plot, null=False)
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


class Transaction(models.Model):
    # One to one?
    record = models.ForeignKey(LandRecord, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    recording_fees = models.FloatField(default=0.0)
    land_tax = models.FloatField(default=0.0)
    building_tax = models.FloatField(default=0.0)
    land_appraised_value = models.FloatField(default=0.0)
    building_appraised_value = models.FloatField(default=0.0)
