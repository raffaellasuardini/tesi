from django.contrib import admin
from .models import Coord

from django.conf import settings

from django.http import JsonResponse

# Register your models here.
@admin.register(Coord)
class CoordAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_coords.html'
    list_display = ('object_label','lat','lng', 'last_update', 'source')

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['GOOGLE_MAP_KEY'] = settings.GOOGLE_MAP_KEY
        return super(CoordAdmin, self).changelist_view(request, extra_context=extra_context)
