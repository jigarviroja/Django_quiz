from django import template

register = template.Library()


@register.filter
def modulo(num, value):
    return num % value
