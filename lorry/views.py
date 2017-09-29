# -*- coding: utf-8 -*-
import logging
import json

from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import JsonResponse

from lorry.models import LorryModel

logger = logging.getLogger(__name__)


class IndexView(View):

    def get(self, request):
        return redirect('/main')


class MainView(View):

    def get(self, request):
        mode = request.GET.get('mode', None)
        if mode == 'all':
            return redirect('/main')

        mode = int(mode) if mode else None
        models = LorryModel.objects.all()
        return render(request, 'lorry/main.html', {'models': models, 'mode': mode})


class ChooseModeAjax(View):

    def post(self, request):
        if request.method == 'POST':
            mode = json.loads(request.POST.get('mode', None))
            print(mode)

            return JsonResponse({'result': True, 'mode': mode})
