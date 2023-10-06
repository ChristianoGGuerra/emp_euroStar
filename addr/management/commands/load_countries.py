import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from addr.models import Country_List


class Command(BaseCommand):
    help = "Loads countries data from CVS file."

    def handle(self, *args, **options):
        data_file = os.path.join(settings.BASE_DIR, 'addr', 'data', 'list_of_countries.csv')

        with open(data_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Country_List.objects.get_or_create(number=row[0], name=row[1], population=row[2], area_km2=row[3])
