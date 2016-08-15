from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from C4D.models import RawLandRecord
from C4D.importer import Importer

class Command(BaseCommand):
    help = "Import an Excel file"
    args = "[excel_file]"
    requires_system_checks = True

    def handle(self, *labels, **options):
        if not labels or len(labels) != 1:
            raise CommandError('Enter one argument, the path to the excel file.')
        excel_file = labels[0]
        importer = Importer(None, excel_file)
        importer.print_to_console = True
        importer.import_file(excel_file)
