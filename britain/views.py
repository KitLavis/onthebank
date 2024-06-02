from django.shortcuts import render
from django.core.serializers import serialize
from .models import Venue


def britain(request):
    venues = Venue.objects.all()
    geojson_data = serialize('geojson', venues, geometry_field='geom')
    context = {'geojson_data': geojson_data}
    return render(request, 'britain.html', context)
