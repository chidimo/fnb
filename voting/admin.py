from django.contrib import admin

from voting.models import Point, Vote


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ["__str__", "points"]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "voter", "contestant", "point"]
