from django import template


register=template.Library()
@register.simple_tag()
def get_effectiveness_tag(product):
    return product.effectiveness.all()


@register.simple_tag()
def get_color_temperature_tag(product):
    return product.color_temperature.all()
