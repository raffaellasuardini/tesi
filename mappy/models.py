from django.db import models

#dati delle coordinate
class Coord (models.Model):
    object_label = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    last_update = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=255, default="backoffice")

    def __str__(self):
        return self.object_label
