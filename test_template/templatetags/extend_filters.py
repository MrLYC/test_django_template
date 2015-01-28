#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()


@register.filter(name="oruser")
def oruser(name):
    """Return name if is not empty or user name
    """
    if name:
        return name
    import getpass
    return getpass.getuser()
