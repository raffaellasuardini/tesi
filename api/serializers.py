from rest_framework import serializers
from mappy.models import Coord

#serializer per la creazione: la label è modificabile
#ma se riceve una label già in db la aggiorna
class CoordSerializer (serializers.ModelSerializer):
    # l'attributo last_update sarà assegnato automaticamente, e quindi non modificabile
    last_update = serializers.DateTimeField(format="%d/%m/%YT%H:%M:%S", read_only=True)
    source = serializers.ReadOnlyField()

    readonly_fields = ['last_update', 'source']
    class Meta:
        model = Coord
        fields = ['id','object_label', 'lat', 'lng', 'last_update', 'source']
    #crea un oggetto coord se la label non è presente in db
    def create(self, validated_data):
        coord, created = Coord.objects.update_or_create(
        object_label=validated_data.get('object_label', None),
        defaults={'lat': validated_data.get('lat', None), 'lng': validated_data.get('lng', None), 'source':'API'})
        return coord
