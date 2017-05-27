# -*- coding: utf-8 -*-

from django.contrib import admin
from rep_api.models import Rep

class RepAdmin(admin.ModelAdmin):
    pass
admin.site.register(Rep, RepAdmin)
