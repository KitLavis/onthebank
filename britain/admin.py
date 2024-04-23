from django.contrib import admin
from .models import Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):

    list_display = (
        "name1",
    )

    search_fields = ['name1']

    ordering = ("name1",)
