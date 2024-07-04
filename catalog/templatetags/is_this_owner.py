from django import template

register = template.Library()

@register.filter
def user_filter(user):
    return user.groups.filter(name__in=['owner']).exists()