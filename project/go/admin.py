from django.contrib import admin

from .models import GoGame

class GoGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(GoGame, GoGameAdmin)
