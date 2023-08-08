from django import template

register = template.Library()


@register.filter
def get_object_fields_and_values(obj):
    fields_and_values = []
    for field in obj._meta.get_fields():
        field_name, field_value = field.name, getattr(obj, field.name)
        fields_and_values.append({'name': field_name, 'value': field_value})
    return fields_and_values
