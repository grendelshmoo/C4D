from xlrd import open_workbook

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

def xls_to_dict(filename):
    book = open_workbook(filename)
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
