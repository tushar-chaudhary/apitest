from .serializers import PincodeSerializer, GetAreaSerializer
from .models import Pincode, PolygonMapping
from rest_framework.response import Response
from rest_framework import generics, permissions, status, views
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from .utils.find_Dist import calcYourself

# Create your views here.

class GetPincodeAPIView(generics.CreateAPIView):

    """
    Endpoint for verifying getting pincode details.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = PincodeSerializer
    queryset = Pincode.objects.all()


class GetLocationAPIView(views.APIView):

    """
    Endpoint for getting location within 5 km radius.

    """

    permission_classes = (permissions.AllowAny, )
    queryset = Pincode.objects.all()

    def get(self, request):
        location = {}
        if(len(request.GET) == 0):
            return Response(status=status.HTTP_200_OK, data=location)
        else:
            latitude = request.GET['latitude']
            longitude = request.GET['longitude']
            pnt = GEOSGeometry('POINT(' + str(longitude) + " " + str(latitude) + ')', srid=4326)
            qs = Pincode.objects.filter(point__distance_lte=(pnt, D(km=5)))
            for obj in qs:
                location[obj.place_name] = obj.key.replace("IN/", "")
            return Response(status=status.HTTP_200_OK, data=location)




class GetLocationYourselfAPIView(views.APIView):

    """
    Endpoint for getting location within 5 km radius yourself.

    """

    permission_classes = (permissions.AllowAny, )
    queryset = Pincode.objects.all()

    def get(self, request):
        location = {}
        if (len(request.GET) == 0):
            return Response(status=status.HTTP_200_OK, data=location)
        else:
            latitude = float(request.GET['latitude'])
            longitude = float(request.GET['longitude'])
            qs = Pincode.pincode.get_latAndlngNotEmpty()
            for obj in qs:
                dist = calcYourself(latitude, float(obj.latitude), longitude, float(obj.longitude))
                if (dist < float(5)):
                    location[obj.place_name] = obj.key.replace("IN/", "")
            return Response(status=status.HTTP_200_OK, data=location)




class GetAreaAPIView(generics.CreateAPIView):

    """
    Endpoint for getting area with multiPolygon.

    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = GetAreaSerializer
    queryset = PolygonMapping.objects.all()




