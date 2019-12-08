from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SightingsForm
from django.db.models import Count
from .models import Squirrel

# Create your views here
def map(request):
    sightings = Sighting.objects.all()[:100]
    context = {'sightings': sightings,}
    return render(request, 'sightings/map.html',context)

def list_sightings(request):
    if request.method == "GET":

        sightings = Sighting.objects.all()
        context = {
                "sightings": Sighting.objects.all(),
        }
        return render(request,'sightings/list.html', context)


def add_sighting(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingForm()

    context = {
            'form': form,
    }

    return render(request, 'sightings/add.html', context)

def edit_view(request, sq_id):

    instance = get_object_or_404(Squirrel, Unique_Squirrel_ID=sq_id)
    form = SightingsForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/{sq_id}')
    
    context ={
        'form':form,
        'sqid':sq_id,
    }
    return render(request, 'sightings/edit.html', context)

def stats(request):

    total_sightings = Sighting.objects.count()
    adult = Sighting.objects.filter(age='Adult').count()
    juvenile = Sighting.objects.filter(age='Juvenile').count()
    gray = Sighting.objects.filter(color='Gray').count()
    cinnamon = Sighting.objects.filter(color='Cinnamon').count()
    black = Sighting.objects.filter(color='Black').count()
    kuks_true = Sighting.objects.filter(kuks=True).count()
    running_true = Sighting.objects.filter(running=True).count()
    eating_true = Sighting.objects.filter(eating=True).count()
    chasing_true = Sighting.objects.filter(chasing=True).count()
    climbing_true = Sighting.objects.filter(climbing=True).count()
    foraging_true = Sighting.objects.filter(foraging=True).count()

    context = {
            'total_sightings': total_sightings,
            'adult':adult,
            'juvenile':juvenile,
            'gray': gray,
            'cinnamon': cinnamon,
            'black': black,
            'kuks': kuks_true,
            'running_true':running_true,
            'eating_true': eating_true,
            'chasing_true': chasing_true,
            'climbing_true': climbing_true,
            'foraging_true': foraging_true,
            }
    return render(request, 'sightings/stats.html', context )
