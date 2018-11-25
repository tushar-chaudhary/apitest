from rest_framework import serializers
from .models import Pincode, MultiplePolygonMapping, PolygonMapping
from django.contrib.gis.geos import GEOSGeometry

class PincodeSerializer(serializers.Serializer):

    pincode = serializers.CharField(
        required=True
    )

    address = serializers.CharField(
        required=True
    )

    city = serializers.CharField(
        required=True
    )

    lng = serializers.CharField(
        required=True, label= "Longitude"
    )

    lat = serializers.CharField(
        required=True, label="Latitude"
    )


    def create(self, validated_data):

        checkLatandLang = Pincode.pincode.get_by_latAndlng(lat=validated_data.get('lat'), lng=validated_data.get('lng'))
        if (checkLatandLang == False):
            pnt = 'SRID=4326;POINT('+ validated_data.get('lng') +' '+ validated_data.get('lat') +')'
            Pincode(key="IN/"+validated_data.get('pincode'), place_name=validated_data.get('address'), admin_name1=validated_data.get('city'), latitude=validated_data.get('lat'), longitude=validated_data.get('lng'), point=pnt
                    ).save()
            return validated_data
        else:
            validated_data["lat"] = checkLatandLang
            validated_data["lng"] = checkLatandLang
            return (validated_data)


class GetAreaSerializer(serializers.Serializer):

    lng = serializers.CharField(
        required=True, label= "Longitude"
    )

    lat = serializers.CharField(
        required=True, label="Latitude"
    )

    locationFound =  serializers.CharField(
        required=False, read_only=True
    )

    def create(self, validated_data):
        locations = {}
        latitude = validated_data.get('lat')
        longitude = validated_data.get('lng')

        pnt = str('SRID=4326;POINT(%s %s)'%(longitude, latitude))
        zone = PolygonMapping.objects.filter(co_ordinates__contains=pnt)
        for area in zone:
            locations[area.name] = {}
            locations[area.name]["type"] = area.type
            locations[area.name]["parent"] = area.parent


        validated_data["locationFound"] = locations



        return validated_data
