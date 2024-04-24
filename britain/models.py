from django.contrib.gis.db import models


class Venue(models.Model):
    name1 = models.CharField(max_length=250)
    identifier = models.CharField(max_length=38, null=True, blank=True)
    startnode = models.CharField(max_length=38, null=True, blank=True)
    endnode = models.CharField(max_length=38, null=True, blank=True)
    form = models.CharField(max_length=50, null=True, blank=True)
    flow = models.CharField(max_length=60, null=True, blank=True)
    fictitious = models.CharField(max_length=5, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    name2 = models.CharField(max_length=250, null=True, blank=True)
    county = models.CharField(max_length=30)
    angclub = models.CharField(max_length=50)
    bank = models.CharField(max_length=50, null=True, blank=True)
    clubsite = models.CharField(max_length=50)
    geom = models.MultiLineStringField(srid=27700)
    bream = models.BooleanField(default=False)
    carp_common = models.BooleanField(default=False)
    carp_crucian = models.BooleanField(default=False)
    carp_koi = models.BooleanField(default=False)
    chub = models.BooleanField(default=False)
    dace = models.BooleanField(default=False)
    grayling = models.BooleanField(default=False)
    minnow = models.BooleanField(default=False)
    perch = models.BooleanField(default=False)
    pike = models.BooleanField(default=False)
    roach = models.BooleanField(default=False)
    rudd = models.BooleanField(default=False)
    salmon = models.BooleanField(default=False)
    tench = models.BooleanField(default=False)
    trout_brown = models.BooleanField(default=False)
    trout_rainbow = models.BooleanField(default=False)
    zander = models.BooleanField(default=False)

    def __string__(self):
        return self.name1

    class Meta:
        ordering = ['name1']
