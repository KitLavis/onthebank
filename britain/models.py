from django.contrib.gis.db import models


class WatercourseLink(models.Model):
    name1 = models.CharField(max_length=250, null=True, blank=True)
    identifier = models.CharField(max_length=38)
    startnode = models.CharField(max_length=38)
    endnode = models.CharField(max_length=38)
    form = models.CharField(max_length=50)
    flow = models.CharField(max_length=60)
    fictitious = models.CharField(max_length=5)
    length = models.IntegerField()
    name2 = models.CharField(max_length=250, null=True, blank=True)
    geom = models.MultiLineStringField(srid=27700)

    def __string__(self):
        return self.name1

    class Meta:
        ordering = ['name1']
