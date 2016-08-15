from __future__ import print_function

import xlrd

from django.conf import settings

from C4D.models import RawLandRecord, ImportLog

class Importer(object):

    def __init__(self, user, print_to_console=True):
        self.user = user
        self.print_to_console = print_to_console
        self.logs = []

        # Start our log
        self.import_log = ImportLog()
        self.import_log.user = user
        self.import_log.save()

    def log_message(self, msg, new_line=True):
        self.logs.append(msg)
        if self.print_to_console:
            if new_line:
                print(msg)
            else:
                print(msg, end="")

    def import_file(self, excel_file):
        self.log_message("Loading '%s'..." % excel_file, new_line=False)
        book = xlrd.open_workbook(excel_file)
        return self.import_data(book)

    def import_data(self, xls_book):
        bad_rows = []
        new_records = []
        rows = self.book_to_dict(xls_book)
        self.log_message(" Loaded %d rows." % len(rows))
        for row_number, row in enumerate(rows):
            try:
                raw_land_record = self.row_to_object(row)
                raw_land_record.save()
                new_records.append(raw_land_record.id)
            except Exception as e:
                bad_rows.append({'row':row_number+1, 'reason':str(e)})

        self.log_message('')
        self.log_message("Saved %d Raw Land Records" % len(new_records))

        if len(bad_rows) > 0:
            self.log_message("Bad data (%d): " % len(bad_rows))
            for r in bad_rows:
                self.log_message("Row %s: %s" % (r['row'], r['reason']))

    def row_to_object(self, row):
        r = RawLandRecord()
        r.import_log = self.import_log
        r.office = row['office']
        r.document_date = row['document_date']
        r.recording_date = row['recording_date']
        r.document_type = row['document_type']
        r.grantor = row['grantor']
        r.grantee = row['grantee']
        r.title_company = row['title_company']
        r.legal_description = row['legal_description']
        r.lot = row['lot']
        r.block = row['block']
        r.tract = row['tract']
        r.unit = row['unit']
        r.area = row['area']
        r.phase = row['phase']
        r.increment = row['increment']
        r.lot_sf = row['square_footage']
        r.building_sf = row['building_square_footage']
        r.map_document = row['map_document']
        r.building_type = row['building_type']
        r.year_built = row['year_built']
        r.construction_type  = row['type_of_construction']
        r.building_condition = row['building_condition']
        r.island = row['island']
        r.municipality = row['municipality']
        r.instrument_number = row['instrument_number']
        r.fy_number = row['fy_number']
        r.lcdn = row['lcdn']
        r.book = row['book']
        r.page = row['page']
        r.amount = row['amount']
        r.recording_fees = row['recording_fees']
        r.land_tax = row['land_tax']
        r.building_tax = row['building_tax']
        r.land_appraised_value = row['land_appraised_value']
        r.building_appraised_value = row['building_appraised_value']
        r.remarks = row['remarks']
        r.cnmi_file_numer = row['cnmi_file_number']
        r.condominium = row['condominium']
        return r

    # def row_to_object(self, row):
    #     rlr = RawLandRecord()
    #     rlr.import_log = self.import_log
    #     rlr.office = row['office']
    #     document_date = row['document_date']
    #     if document_date:
    #         rlr.document_date = xlrd.xldate.xldate_as_datetime(document_date, 0)
    #     recording_date = row['recording_date']
    #     if recording_date:
    #         rlr.recording_date = xlrd.xldate.xldate_as_datetime(recording_date, 0)
    #     rlr.document_type = row['document_type']
    #     rlr.grantor = row['grantor']
    #     rlr.grantee = row['grantee']
    #     rlr.title_company = row['title_company']
    #     rlr.legal_description = row['legal_description']
    #     rlr.lot = row['lot']
    #     rlr.block = row['block']
    #     rlr.tract = row['tract']
    #     rlr.unit = row['unit']
    #     area = row['area']
    #     if area:
    #         rlr.area = area
    #     rlr.phase = row['phase']
    #     increment = row['increment']
    #     if increment:
    #         rlr.increment = increment
    #     lot_sf = row['square_footage']
    #     if lot_sf:
    #         rlr.lot_sf = lot_sf
    #     building_sf = row['building_square_footage']
    #     if building_sf:
    #         rlr.building_sf = building_sf
    #     map_document = row['map_document']
    #     if map_document:
    #         rlr.map_document = map_document
    #     rlr.building_type = row['building_type']
    #     year_built = row['year_built']
    #     if year_built:
    #         rlr.year_built = year_built
    #     rlr.construction_type  = row['type_of_construction']
    #     rlr.building_condition = row['building_condition']
    #     rlr.island = row['island']
    #     rlr.municipality = row['municipality']
    #     rlr.instrument_number = row['instrument_number']
    #     rlr.fy_number = row['fy_number']
    #     lcdn = row['lcdn']
    #     if lcdn:
    #         rlr.lcdn = lcdn
    #     book = row['book']
    #     if book:
    #         rlr.book = book
    #     page = row['page']
    #     if page:
    #         rlr.page = page
    #     amount = row['amount']
    #     if amount:
    #         rlr.amount = amount
    #     recording_fees = row['recording_fees']
    #     if recording_fees:
    #         rlr.recording_fees = recording_fees
    #     land_tax = row['land_tax']
    #     if land_tax:
    #         rlr.land_tax = land_tax
    #     building_tax = row['building_tax']
    #     if building_tax:
    #         rlr.building_tax = bulding_tax
    #     lav = row['land_appraised_value']
    #     if lav:
    #         rlr.land_appraised_value = lav
    #     bav = row['building_appraised_value']
    #     if bav:
    #         rlr.building_appraised_value = bav
    #     rlr.remarks = row['remarks']
    #     if 'cnmi_file_number' in row:
    #         rlr.cnmi_file_numer = row['cnmi_file_number']
    #     if 'condominium' in row:
    #         rlr.condominium = row['condominium']
    #
    #     return rlr

    def book_to_dict(self, book):
        sheet = book.sheet_by_index(0)
        keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
        dict_list = []
        for row_index in xrange(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                for col_index in xrange(sheet.ncols)}
            dict_list.append(d)
        return dict_list
