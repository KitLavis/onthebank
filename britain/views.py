from django.shortcuts import render
from .models import WatercourseLink


def index(request):
    watercourse_links = WatercourseLink.objects.all()
    context = {}
    context['watercourse_links'] = watercourse_links
    return render(request, 'index.html', context)
