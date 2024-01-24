from django import template

register = template.Library()


@register.filter
def to_lower(value):
    return value.lower()


@register.filter
def to_cap(value):
    kir = value.split()
    an = ''
    for i, j in enumerate(kir):
        an += j.capitalize()
        z = len(kir)
        if i != z - 1:
            an += ' '
    return an


@register.filter
def to_kir(value):
    return value.title()
