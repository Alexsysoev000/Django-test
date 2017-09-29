# -*- coding: utf-8 -*-

from django.db import models


class LorryModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    lifting_capacity = models.FloatField()


class Lorry(models.Model):
    pennant_number = models.CharField(max_length=255)
    current_weight = models.FloatField()
    model = models.ForeignKey(LorryModel)

    @property
    def overweight(self):
        ratio = self.current_weight / self.model.lifting_capacity
        return 0 if ratio < 1 else (ratio - 1) * 100
