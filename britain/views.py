from django.shortcuts import render
from .models import WatercourseLink


def index(request):
    river_avon = WatercourseLink.objects.filter(name1='River Avon')
    context = {}
    context['river_avon'] = river_avon
    return render(request, 'index.html', context)
