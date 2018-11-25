from django.contrib import admin
from .models import Pincode, PolygonMapping, MultiplePolygonMapping

# Register your models here.

admin.site.register(Pincode)
admin.site.register(PolygonMapping)
admin.site.register(MultiplePolygonMapping)