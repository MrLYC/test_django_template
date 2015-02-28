{% load sqllike_filters %}


{{ model | where:"`val` % 2 == 1" | select:"key = name, val"}}
