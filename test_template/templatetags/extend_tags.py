#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


@register.simple_tag(name="random_choice")
def random_choice(*args):
    import random
    return random.choice(args)


@register.simple_tag(name="var")
def var(namespace, **kw):
    """set var to namespace from kw
    """
    for k, v in kw.iteritems():
        namespace[k] = v
    return ""


@register.simple_tag(name="listvar")
def listvar(namespace, var, *values):
    """set list var to namespace
    """
    namespace[var] = [i for i in values if i]
    return ""
