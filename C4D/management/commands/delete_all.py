from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from C4D.models import RawLandRecord

class Command(BaseCommand):
    help = "Delete all Raw Land Records"
    requires_system_checks = False

    def handle(self, *labels, **options):
        print("Deleting %d RawLandRecord objects!" % RawLandRecord.objects.all().count())
        RawLandRecord.objects.all().delete()
