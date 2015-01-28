#!/usr/bin/env python
# encoding: utf-8

from django.views.generic.base import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        return render(request, "index.tpl")
