from django.contrib.gis.db import models
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
    ]

class PincodeManager(models.Manager):
    def get_by_latAndlng(self, lat, lng):
        qs = self.get_queryset().filter(latitude=lat, longitude=lng)
        if qs.count() > 0:
            return 'Latitude and Longitude already exists'
        else:
            return False

    def get_latAndlngNotEmpty(self):
        qs = self.get_queryset().filter(latitude__isnull=False, longitude__isnull=False)
        return qs




class Pincode(models.Model):
    key = models.CharField(max_length=50, primary_key=True, null=False, blank=False)
    place_name = models.CharField(max_length=50, null=True, blank=True)
    admin_name1 = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    accuracy = models.CharField(max_length=50, null=True, blank=True)
    point = models.PointField(srid=4326, null=True, blank=True)
    objects = models.Manager()  # The default manager.
    pincode = PincodeManager()

    def __str__(self):  # __unicode__ for Python 2
        return (self.place_name + "-" + self.latitude + "/" + self.longitude)

    class Meta:
        verbose_name = 'pincode'


class PolygonMapping(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    parent = models.CharField(max_length=50, blank=True, null=True)
    co_ordinates = models.PolygonField(blank=True, null=True)
    objects = models.Manager()  # The default manager.

    def __str__(self):  # __unicode__ for Python 2
        return (self.name + "-" + self.type + "-" + self.parent)

    class Meta:
        verbose_name = 'polygonmapping'

class MultiplePolygonMapping(models.Model):
    id = models.IntegerField(primary_key=True)
    co_ordinates = models.MultiPolygonField(blank=True, null=True)
    objects = models.Manager()  # The default manager.

    def __str__(self):  # __unicode__ for Python 2
        return str('OverlappedBoundary')

    class Meta:
        verbose_name = 'multiplepolygonmapping'



