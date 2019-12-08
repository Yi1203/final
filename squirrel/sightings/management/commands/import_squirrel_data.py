from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import requests, csv, sys
import datetime
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    help ='Import squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be imported')

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        

        with open(path, mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            USID = set()
            for row in reader:
                if row.get('Unique Squirrel ID') in USID:
                    continue
                else:
                    obj, created = Squirrel.objects.get_or_create(
                        X = row.get('X'),
                        Y = row.get('Y'),
                        USID = row.get('Unique Squirrel ID'),
                        Hectare = row.get('Hectare'),
                        Shift = row.get('Shift'),
                        Date = datetime.datetime.strptime(row.get('Date').strip(),'%m%d%Y').date() if row.get('Date') else None,
                        HSN = row.get('Hectare Squirrel Number'),
                        Age = row.get('Age'),
                        PFC = row.get('Primary Fur Color'),
                        HFC = row.get('Highlight Fur Color'),
                        CPHC = row.get('Combination of Primary and Highlight Color'),
                        CN = row.get('Color Notes'),
                        Location = row.get('Location'),
                        SL = row.get('Specific Location'),
                        Running = row.get('Running'),
                        Chasing = row.get('Chasing'),
                        Climbing = row.get('Climbing'),
                        Eating = row.get('Eating'),
                        Foraging = row.get('Foraging'),
                        OA = row.get('Other Activities'),
                        Kuks = row.get('Kuks'),
                        Quaas = row.get('Quaas'),
                        Moans = row.get('Moans'),
                        TF = row.get('Tail flags'),
                        TT = row.get('Tail twitches'),
                        Approaches = row.get('Approaches'),
                        Indifferent = row.get('Indifferent'),
                        RF = row.get('Runs from'),
                        OI = row.get('Other Interactions'),
                        LL = row.get('Lat/Long'),
                        Zip = row.get('Zip Codes'),
                        CD = row.get('Community Districts'),
                        BB = row.get('Borough Boundaries'),
                        CCD = row.get('City Council Districts'),
                        PP = row.get('Police Precincts'),
                     )
                USID.add(row.get('Unique Squirrel ID'))
        print('Done!')
