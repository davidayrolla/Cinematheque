from django import template

register = template.Library()


@register.filter
def get_class_name(value):
    # return value.__class__.__name__
    if f'{value._meta.verbose_name}'.capitalize() != f'{value.__class__.__name__}'.capitalize() :
        str = f'{value._meta.verbose_name}'
    else:
        str = f'{value.__class__.__name__}'.capitalize()
    return str


@register.filter
def get_class_plural_name(value):
    if f'{value._meta.verbose_name_plural}'.capitalize() != f'{value.__class__.__name__}'.capitalize() + 's':
        str = f'{value._meta.verbose_name_plural}'
    else:
        str = value.__class__.__name__ + 's'
    return str


register.filter('get_class_name', get_class_name)
register.filter('get_class_plural_name', get_class_plural_name)
