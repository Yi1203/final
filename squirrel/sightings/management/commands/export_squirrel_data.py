from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'exports all fields'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help='filepath name')
    
    def handle(self, *args, **kwargs):
        with open('file_pathv', mode='w',newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            all_fields = [x.name for x in Squirrel._meta.get_fields()]
            fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields[1:]]
            writer.writerow(fieldnames)
            for j in range(len(Squirrel.objects.all())):
                rowval=list()
                for i in all_fields:
                    if i == 'id': continue
                    rowval.append(getattr(Squirrel.objects.all()[j],i))
                writer.writerow(rowval)
        csvfile.close
