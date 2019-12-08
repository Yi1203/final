from django.core.management.base import BaseCommand
from sightings.models import Squirrel
from django.utils import timezone
import pandas as pd
import numpy as np
import csv

class Command(BaseCommand):
    help ='Import squirrel data from NYC Central Park'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='path of file to be imported')

    def handle(self, *args, **options):
        path = options['path']
        df = pd.read_csv(path)
        for item in df.iterrows():
            item=item[1]
            s = Squirrel(
                Y=item['Y'],
                X=item['X'],
                USID = item['Unique Squirrel ID'],
                Shift = item['Shift'],
                Date = timezone.datetime(int(str(item['Date'])[-4:]),int(str(item['Date'])[:2]),int(str(item['Date'])[2:4])).date(),
                Age = item['Age'],
                PFC = item['Primary Fur Color'],
                Location = item['Location'],                                                           
                SL = item['Specific Location'],
                Running = item['Running'],
                Chasing = item['Chasing'],
                Climbing = item['Climbing'],
                Eating = item['Eating'],
                Foraging = item['Foraging'],
                OA = item['Other Activities'],
                Kuks = item['Kuks'],
                Quaas = item['Quaas'],
                Moans = item['Moans'],
                TF = item['Tail flags'],
                TT = item['Tail twitches'],
                Approaches = item['Approaches'],
                Indifferent = item['Indifferent'],
                RF = item['Runs from'],
                )
            s.save()                  
    print('ok!')
