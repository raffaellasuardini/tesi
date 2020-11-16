from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from mappy.models import Coord
from .serializers import CoordSerializer , CoordLabelROSerializer


class CoordListCreate (generics.ListCreateAPIView):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class CoordRetrieveUpdateDestroy (generics.RetrieveUpdateDestroyAPIView):
    queryset = Coord.objects.all()
    serializer_class = CoordLabelROSerializer
    permission_classes = [IsAdminUser]

# class CoordViewSet (viewsets.ModelViewSet):
#     queryset = Coord.objects.all()
#     serializer_class = CoordSerializer
#     permission_classes = [AdminPermission]
