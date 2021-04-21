from django.contrib import admin

from voting.models import Point

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'points']
