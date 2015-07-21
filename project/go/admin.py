from django.contrib import admin

from .models import GoGame, GoUser

class GoGameAdmin(admin.ModelAdmin):
    pass

admin.site.register(GoGame, GoGameAdmin)

admin.site.register(GoUser)