from django.contrib import admin

from Tournaments import models
from Tournaments.models import Tournament


# Register your models here.

class TournamentListAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ('title', 'mode', 'prize', 'ticketamount', 'is_active', 'is_delete')


admin.site.register(models.Tournament, TournamentListAdmin)
admin.site.register(models.Category)