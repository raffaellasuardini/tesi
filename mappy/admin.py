from django.contrib import admin
from .models import Coord

from django.http import JsonResponse

# Register your models here.
@admin.register(Coord)
class CoordAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_coords.html'
    list_display = ('object_label','lat','lng', 'last_update')
