# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Rep(models.Model):
    name = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2)
    district = models.CharField(max_length=255)
    killed = models.IntegerField(null=True, blank=True)
    debt = models.IntegerField(null=True, blank=True)
    uninsured = models.IntegerField(null=True, blank=True)
