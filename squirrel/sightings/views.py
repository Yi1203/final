from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SightingsForm
from django.db.models import Count
from .models import Squirrel
import random
# Create your views here
def map(request):

    sightings = Squirrel.objects.all()[:100]
    context = {'sightings': sightings,}
    return render(request, 'sightings/map.html',context)

def list(request):
    if request.method == "GET":

        sightings = Squirrel.objects.all()
        context = {
                "sightings": Squirrel.objects.all(),
        }
        return render(request,'sightings/list.html', context)


def add(request):
    if request.method == 'POST':
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingsForm()

    context = {
            'form': form,
    }

    return render(request, 'sightings/add.html', context)

def edit(request, USID):

    instance = get_object_or_404(Squirrel, pk=USID)
    form = SightingsForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/{USID}')
    
    context ={
        'form':form,
        'USID':USID,
    }
    return render(request, 'sightings/edit.html', context)

def stats(request):

    total_sightings = Squirrel.objects.count()
    adult = Squirrel.objects.filter(Age='Adult').count()
    juvenile = Squirrel.objects.filter(Age='Juvenile').count()
    gray = Squirrel.objects.filter(PFC='Gray').count()
    cinnamon = Squirrel.objects.filter(PFC='Cinnamon').count()
    black = Squirrel.objects.filter(PFC='Black').count()
    running_true = Squirrel.objects.filter(Running=True).count()
    eating_true = Squirrel.objects.filter(Eating=True).count()
    chasing_true = Squirrel.objects.filter(Chasing=True).count()
    climbing_true = Squirrel.objects.filter(Climbing=True).count()
    foraging_true = Squirrel.objects.filter(Foraging=True).count()

    context = {
            'total_sightings': total_sightings,
            'adult':adult,
            'juvenile':juvenile,
            'gray': gray,
            'cinnamon': cinnamon,
            'black': black,
            'running_true':running_true,
            'eating_true': eating_true,
            'chasing_true': chasing_true,
            'climbing_true': climbing_true,
            'foraging_true': foraging_true,
            }
    return render(request, 'sightings/stats.html', context )
