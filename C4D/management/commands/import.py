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
            document_date = row['document_date']
            if document_date:
                rlr.document_date = xlrd.xldate.xldate_as_datetime(document_date, 0)
            recording_date = row['recording_date']
            if recording_date:
                rlr.recording_date = xlrd.xldate.xldate_as_datetime(recording_date, 0)
            rlr.title_company = row['title_company']
            rlr.legal_description = row['legal_description']
            rlr.lot = row['lot']
            rlr.block = row['block']
            rlr.unit = row['unit']
            area = row['area']
            if area:
                rlr.area = area
            rlr.phase = row['phase']
            tract = row['tract']
            if tract:
                rlr.tract = tract
            increment = row['increment']
            if increment:
                rlr.increment = increment
            lot_sf = row['square_footage']
            if lot_sf:
                rlr.lot_sf = lot_sf
            building_sf = row['building_square_footage']
            if building_sf:
                rlr.building_sf = building_sf
            map_document = row['map_document']
            if map_document:
                rlr.map_document = map_document
            rlr.building_type = row['building_type']
            year_built = row['year_built']
            if year_built:
                rlr.year_built = year_built
            rlr.construction_type  = row['type_of_construction']
            rlr.building_condition = row['building_condition']
            rlr.island = row['island']
            rlr.municipality = row['municipality']
            rlr.instrument_number = row['instrument_number']
            rlr.fy_number = row['fy_number']
            lcdn = row['lcdn']
            if lcdn:
                rlr.lcdn = lcdn
            book = row['book']
            if book:
                rlr.book = book
            page = row['page']
            if page:
                rlr.page = page
            amount = row['amount']
            if amount:
                rlr.amount = amount
            recording_fees = row['recording_fees']
            if recording_fees:
                rlr.recording_fees = recording_fees
            land_tax = row['land_tax']
            if land_tax:
                rlr.land_tax = land_tax
            building_tax = row['building_tax']
            if building_tax:
                rlr.building_tax = bulding_tax
            lav = row['land_appraised_value']
            if lav:
                rlr.land_appraised_value = lav
            bav = row['building_appraised_value']
            if bav:
                rlr.building_appraised_value = bav
            rlr.remarks = row['remarks']
            if 'cnmi_file_number' in row:
                rlr.cnmi_file_numer = row['cnmi_file_number']
            if 'condominium' in row:
                rlr.condominium = row['condominium']

            rlr.save()
            print(".")
