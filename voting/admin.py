from django.contrib import admin

from voting.models import Vote

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'points']
