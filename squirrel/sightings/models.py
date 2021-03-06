from django.db import models

# Create your models here

class Squirrel(models.Model):
    X=models.FloatField(null=True)
    Y=models.FloatField(null=True)
    USID=models.CharField(max_length=100,verbose_name='Unique Squirrel ID',primary_key=True,default = None)
    Hectare=models.CharField(max_length=100,null=True)
    Shift=models.CharField(max_length=100,null=True)
    Date=models.DateField(null=True)
    HSN=models.IntegerField(verbose_name='Hectare Squirrel Number',null=True)
    Age=models.CharField(max_length=100,null=True)
    PFC=models.CharField(max_length=100,verbose_name='Primary Fur Color',null=True)
    HFC=models.CharField(max_length=100,verbose_name='Highlight Fur Color',null=True)
    CPHC=models.CharField(max_length=100,verbose_name='Combination of Primary and Highlight Color',null=True)
    CN=models.CharField(max_length=100,verbose_name='Color notes',null=True)
    Location=models.CharField(max_length=100,null=True)
    AGSM=models.IntegerField(verbose_name='Above Ground Sighter Measurement',null=True)
    SL=models.CharField(max_length=100,verbose_name='Specific Location',null=True)
    Running=models.BooleanField(null=True)
    Chasing=models.BooleanField(null=True)
    Climbing=models.BooleanField(null=True)
    Eating=models.BooleanField(null=True)
    Foraging=models.BooleanField(null=True)
    OA=models.CharField(max_length=100,verbose_name='Other Activities',null=True)
    Kuks=models.BooleanField(null=True)
    Quaas=models.BooleanField(null=True)
    Moans=models.BooleanField(null=True)
    TF=models.BooleanField(verbose_name='Tail flags',null=True)
    TT=models.BooleanField(verbose_name='Tail twitches',null=True)
    Approaches=models.BooleanField(null=True)
    Indifferent=models.BooleanField(null=True)
    RF=models.BooleanField(verbose_name='Runs from',null=True)
    OI=models.CharField(max_length=100,verbose_name='Other Interactions',null=True)
    LL=models.CharField(max_length=100,verbose_name='Lat/Long',null=True)
    Zip=models.IntegerField(verbose_name='Zip Codes',null=True)
    CD=models.IntegerField(verbose_name='Community Districts',null=True)
    BB=models.IntegerField(verbose_name='Borough Boundaries',null=True)
    CCD=models.IntegerField(verbose_name='City Council Districts',null=True)
    PP=models.IntegerField(verbose_name='Police Precincts',null=True)

    def __str__(self):
         return self.USID
