# -*- coding: utf-8 -*-
import os
import sys

import django

sys.path.insert(0, os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'
django.setup()

from lorry.models import LorryModel, Lorry  # noqa


if __name__ == '__main__':
    lorry_model1, created = LorryModel.objects.get_or_create(name='БЕЛАЗ', lifting_capacity=120)
    lorry_model2, created = LorryModel.objects.get_or_create(name='Komatsu', lifting_capacity=110)
    Lorry.objects.get_or_create(pennant_number='101', current_weight=100, model=lorry_model1)
    Lorry.objects.get_or_create(pennant_number='102', current_weight=125, model=lorry_model1)
    Lorry.objects.get_or_create(pennant_number='K103', current_weight=120, model=lorry_model2)

    lorry_models = LorryModel.objects.all()
    lorries = lorry_model1.lorry_set.all()

    for lorry in lorries:
        print(lorry.pennant_number)
