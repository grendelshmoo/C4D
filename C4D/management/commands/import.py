import xlrd

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from C4D.models import RawLandRecord

def xls_to_dict(filename):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
    dict_list = []
    for row_index in xrange(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value
            for col_index in xrange(sheet.ncols)}
        dict_list.append(d)
    return dict_list

class Command(BaseCommand):
    help = "Import an Excel file"
    args = "[import_file]"
    requires_system_checks = True

    def handle(self, *labels, **options):
        if not labels or len(labels) != 1:
            raise CommandError('Enter one argument, the path to the excel file.')
        excel_file = labels[0]

        # Load our excel file
        print("Loading '%s'..." % excel_file)
        rows = xls_to_dict(excel_file)
        print("Success!  Loaded %d rows." % len(rows))

        for row in rows:
            rlr = RawLandRecord()
            rlr.office = row['office']
            rlr.document_date = xlrd.xldate.xldate_as_datetime(row['document_date'], 0)
            rlr.recording_date = xlrd.xldate.xldate_as_datetime(row['recording_date'], 0)
            rlr.title_company = row['title_company']
            rlr.legal_description = row['legal_description']
            rlr.lot = row['lot']
            rlr.block = row['block']
            rlr.unit = row['unit']
            rlr.area = row['area']
            rlr.phase = row['phase']
            rlr.tract = row['tract']
            rlr.increment = row['increment']
            rlr.lot_sf = row['square_footage']
            rlr.building_sf = row['building_square_footage']
            rlr.map_document = row['map_document']
            rlr.building_type = row['building_type']
            rlr.year_built = row['year_built']
            rlr.construction_type  = row['type_of_construction']
            rlr.building_condition = row['building_condition']
            rlr.island = row['island']
            rlr.municipality = row['municipality']
            rlr.condominium = row['condominium']
            rlr.instrument_number = row['instrument_number']
            rlr.fy_number = row['fy_number']
            rlr.cnmi_file_numer = row['cnmi_file_numer']
            rlr.lcdn = row['lcdn']
            rlr.book = row['book']
            rlr.page = row['page']
            rlr.amount = row['lcdn']
            rlr.recording_fees = row['recording_fees']
            rlr.land_tax = row['land_tax']
            rlr.building_tax = row['building_tax']
            rlr.land_appraised_value = row['land_appraised_value']
            rlr.building_appraised_value = row['building_appraised_value']
            rlr.remarks = row['remarks']
            rlr.save()
