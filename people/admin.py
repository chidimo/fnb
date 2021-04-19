from django.contrib import admin
from django.contrib.auth.models import Group

from people.models import AppUser, Person, PersonVote
from people.forms import PersonChangeForm, PersonCreationForm

# admin.site.unregister(Group)

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    form = PersonChangeForm
    add_form = PersonCreationForm

    list_filter = ('is_admin', )
    list_editable = ['is_admin']
    list_display = ['email', 'is_admin', 'person', 'is_active', 'last_login']
    fieldsets = (
        ('Login', {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('is_admin',
                                    'is_active', 'is_superuser', 'groups',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2',)}
         ),
    )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_editable = ['phone', 'is_contestant', 'profile_pix']
    list_display = ['name', 'phone', 'vote_count', 'cast_votes', 'is_contestant', 'sex', 'profile_pix']

@admin.register(PersonVote)
class PersonVoteAdmin(admin.ModelAdmin):
    list_display = ['voter', 'voted_for', 'vote']
