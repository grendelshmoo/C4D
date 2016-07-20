from django.contrib import admin

from models import *

class RawLandRecordAdmin(admin.ModelAdmin):
    search_fields = ('legal_description', 'lot')
    list_display=('id', 'office', 'island', 'document_date', 'legal_description')
    list_filter=('office', 'island')
admin.site.register(RawLandRecord, RawLandRecordAdmin)

# Normalized tables for later version
#admin.site.register(Office)
#admin.site.register(LandRecord)
#admin.site.register(Property)
#admin.site.register(TitleCompany)
#admin.site.register(Municipality)
#admin.site.register(Island)
#admin.site.register(Condominium)
#admin.site.register(Transaction)
