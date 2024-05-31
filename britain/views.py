from django.shortcuts import render
from django.core.serializers import serialize
from .models import Venue


def index(request):
    venues = Venue.objects.all()
    geojson_data = serialize('geojson', venues, geometry_field='geom')
    context = {'geojson_data': geojson_data}
    return render(request, 'templates/britain/index.html', context)
