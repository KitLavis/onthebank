from django.contrib import admin
from .models import WatercourseLink

@admin.register(WatercourseLink)
class WatercourseLinkAdmin(admin.ModelAdmin):

    list_display = (
        "name1",
    )

    search_fields = ['name1']

    ordering = ("name1",)
