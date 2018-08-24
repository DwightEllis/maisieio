from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(value, objectlist):
    """  This is required to lookup attributes by named variable

    Returns an empty dictionary if not present to allow chaining
    """
    return value.get(objectlist)
    target = value
    for field in objectlist:
        nextval = target.get(field)
    return nextval
