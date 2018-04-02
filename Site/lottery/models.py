# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class LottreyNums(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    num_1 = models.CharField(max_length=2)
    num_2 = models.CharField(max_length=2)
    num_3 = models.CharField(max_length=2)
    num_4 = models.CharField(max_length=2)
    num_5 = models.CharField(max_length=2)
    num_6 = models.CharField(max_length=2)
