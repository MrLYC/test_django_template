#!/usr/bin/env python
# encoding: utf-8

from django.views.generic.base import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        tpl = request.GET.get("tpl", "index")
        return render(request, "%s.tpl" % tpl)


class TestCache(View):
    def get(self, request):
        return render(request, "cache.tpl", {"cache": {}})


class TestSQL(View):
    def get(self, request):
        return render(request, "sql.tpl", {"model": [
            {"name": 0, "val": 2}, {"name": 1, "val": 1}, {"name": 2, "val": 3}]})
