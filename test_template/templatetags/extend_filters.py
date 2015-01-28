#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


@register.filter(name="random_choice")
def random_choice(*args):
    """Return random.choice(args)
    """
    import random
    return random.choice(args)


@register.filter(name="type")
def type_(value):
    """Return type(value)
    """
    return type(value)


@register.filter(name="oruser")
def oruser(name):
    """Return name if is not empty or user name
    """
    if name:
        return name
    import getpass
    return getpass.getuser()


@register.filter(name="getattr")
def getattr(obj, attr):
    """Return getattr(obj, attr)
    """
    return getattr(obj, attr)


@register.filter(name="hasattr")
def hasattr(obj, attr):
    """Return hasattr(obj, attr)
    """
    return hasattr(obj, attr)


@register.filter(name="getkey")
def getkey(dict_, key, default=None):
    """Return dict_.get(key, default)
    """
    return dict_.get(key, default)


@register.filter(name="haskey")
def haskey(dict_, key):
    """Return dict_.haskey(key))
    """
    return dict_.haskey(key)
