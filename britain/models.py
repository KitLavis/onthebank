from django.contrib.gis.db import models


class Venue(models.Model):
    name1 = models.CharField(max_length=250)
    identifier = models.CharField(max_length=38)
    startnode = models.CharField(max_length=38)
    endnode = models.CharField(max_length=38)
    form = models.CharField(max_length=50)
    flow = models.CharField(max_length=60)
    fictitious = models.CharField(max_length=5)
    length = models.IntegerField()
    name2 = models.CharField(max_length=250)
    county = models.CharField(max_length=30)
    angclub = models.CharField(max_length=50)
    bank = models.CharField(max_length=10)
    clubsite = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=27700)

    def __string__(self):
        return self.name1

    class Meta:
        ordering = ['name1']
