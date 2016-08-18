from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from C4D.importer import Exporter
from models import ImportLog, RawLandRecord

@admin.register(RawLandRecord)
class RawLandRecordAdmin(admin.ModelAdmin):

    def export_xls(modeladmin, request, queryset):
        if queryset.count() > 65532:
            messages.add_message(request, messages.ERROR, "Exports must be limited to 65532 rows or less!")
            return
        exporter = Exporter()
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s' % exporter.file_name
        exporter.export_xls(response, queryset)
        return response
    export_xls.short_description = "Export XLS File"

    #search_fields = ('legal_description', 'lot')
    list_display = ('__unicode__', 'document_date', 'recording_date', 'document_type', 'grantor', 'grantee' )
    list_filter = ('office', 'island')
    list_per_page = 40
    actions = ['export_xls', ]
    exclude = ('import_log', )

    def has_change_permission(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        if request.user.is_superuser:
            return True
        return (request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)) or
               request.user.has_perm('%s.change_%s' % (ct.app_label, ct.model)) )

    def get_readonly_fields(self, request, obj=None):
        ct = ContentType.objects.get_for_model(self.model)
        if not request.user.is_superuser and request.user.has_perm('%s.view_%s' % (ct.app_label, ct.model)):
            return [el.name for el in self.model._meta.fields]
        return self.readonly_fields


class RawLandRecordInline(admin.TabularInline):
    model = RawLandRecord
    max_num = 10
    fields = ('legal_description', 'lot', 'block', 'tract')
    readonly_fields = ('legal_description', 'lot', 'block', 'tract')
    can_delete = False


@admin.register(ImportLog)
class ImportLogAdmin(admin.ModelAdmin):

    def records(self):
        return RawLandRecord.objects.filter(import_log=self).count()

    list_display = ('id', 'imported_by', 'start_ts', 'file_name', records)
    fields = ('imported_by', 'start_ts', 'end_ts', 'file_name')
    readonly_fields = ('start_ts', 'end_ts')
    #inlines = [
    #    RawLandRecordInline,
    #]



# Normalized tables for later version
#admin.site.register(Office)
#admin.site.register(LandRecord)
#admin.site.register(Property)
#admin.site.register(TitleCompany)
#admin.site.register(Municipality)
#admin.site.register(Island)
#admin.site.register(Condominium)
#admin.site.register(Transaction)
