#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


@register.simple_tag(name="random_choice")
def random_choice(*args):
    import random
    return random.choice(args)
