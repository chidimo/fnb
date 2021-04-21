from django.contrib import admin

from people.models import AppUser, Person
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
    list_display = ['__str__', 'name', 'phone', 'votes_cast', 'received_votes', 'is_contestant', 'sex', 'profile_pix']
