from django.http import HttpResponse
from django.conf import settings
from rest_framework import generics
from mappy.models import Coord
from .serializers import CoordSerializer


class CoordCreate (generics.CreateAPIView):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class CoordList (generics.ListAPIView):
    serializer_class = CoordSerializer


    def get_queryset(self):
        token = self.request.query_params.get('token', None)
        if token == settings.TOKEN:
            return Coord.objects.all()
        else:
            return HttpResponse(status=500)
