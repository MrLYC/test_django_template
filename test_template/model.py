#!/usr/bin/env python
# encoding: utf-8

from django.db import models


class Person(models.Model):
    name = models.CharField(default="")
    age = models.IntegerField(default=0)
