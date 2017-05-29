# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Rep(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2)
    district = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, blank=True)
    killed = models.IntegerField(null=True, blank=True)
    debt = models.IntegerField(null=True, blank=True)
    uninsured = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    medicaid_expansion_state = models.BooleanField(default=False)
    swing_left_district = models.BooleanField(default=False)
    freedom_caucus_member = models.BooleanField(default=False)
    percent_vote_2016 = models.FloatField(default=0)
    percent_vote_clinton = models.FloatField(default=0)
    percent_vote_trump = models.FloatField(default=0)
    president_vote_margin = models.FloatField(default=0)
    twitter_link = models.CharField(max_length=255, blank=True)
    facebook_link = models.CharField(max_length=255, blank=True)
    twitter_handle = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name