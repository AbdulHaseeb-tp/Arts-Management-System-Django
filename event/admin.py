from django.contrib import admin

from . models import Event, Registration, SuggestionBox
# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event', 'position', 'point')

    # search_fields = ['id']



admin.site.register(Event)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(SuggestionBox)