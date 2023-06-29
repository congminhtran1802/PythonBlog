from django import template

register = template.Library()

@register.filter
def find(string, char):
    print("vị trí:",string.find(char))
    return string.find(char)