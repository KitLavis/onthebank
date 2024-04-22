from django.shortcuts import render
from .models import WatercourseLink


def index(request):
    test_link = WatercourseLink.objects.get(identifier='DC6C6B09-67D0-4F01-9089-F4E8C5D0DEBF')
    context = {}
    context['test_link'] = test_link
    return render(request, 'index.html', context)
