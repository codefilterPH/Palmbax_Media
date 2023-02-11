from django import template
register = template.Library()


@register.filter
def add_thousand_separator(number):
    if number is None:
        return ''
    return '{:,}'.format(number)
