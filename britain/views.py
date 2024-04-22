from django.shortcuts import render
from django.core.serializers import serialize
from .models import WatercourseLink


def index(request):
    river_avon = WatercourseLink.objects.filter(name1='River Avon')
    geojson_data = serialize('geojson', river_avon, geometry_field='geom')
    context = {'geojson_data': geojson_data}
    return render(request, 'index.html', context)
