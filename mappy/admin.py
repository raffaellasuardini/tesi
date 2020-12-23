from django.contrib import admin
from .models import Coord

from django.conf import settings

from django.http import JsonResponse

# Register your models here.
@admin.register(Coord)
class CoordAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list_coords.html'
    list_display = ('object_label','lat','lng', 'last_update', 'source')
    exclude = ('source',)

    def save_model(self, request, obj, form, change):
        obj.source= 'backoffice'
        obj.save()
        return super().save_model(request, obj, form, change)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['GOOGLE_MAP_KEY'] = settings.GOOGLE_MAP_KEY
        return super(CoordAdmin, self).changelist_view(request, extra_context=extra_context)
