# -*- coding: utf-8 -*-

from django.contrib import admin
from rep_api.models import Rep

class RepAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'state')
    
admin.site.register(Rep, RepAdmin)
