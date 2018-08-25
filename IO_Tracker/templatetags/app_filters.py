from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(value, objectlist):
    """  Allows lookup of attributes by the value of a variable, not a literal string 

    Returns an empty dictionary if not present to allow chaining
    """
    return value.get(objectlist)
