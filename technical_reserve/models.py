# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.


class TechnicalReserve(models.Model):
    code = models.IntegerField(blank=True, default=0, unique=True)
    length = models.FloatField(blank=True)
    lattitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
