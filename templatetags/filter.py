from django import template

register = template.Library()


@register.filter
def get_class_name(value):
    return value.__class__.__name__


@register.filter
def get_class_plural_name(value):
    str = f'{value._meta.verbose_name_plural}'
    return str.capitalize()


register.filter('get_class_name', get_class_name)
register.filter('get_class_plural_name', get_class_plural_name)
