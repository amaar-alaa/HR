from __future__ import unicode_literals
from django import template


register = template.Library()

@register.filter(name='has_group')

def has_group(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False

#in template to check groubs and add this tags in above page {% load user_tags %}
# {% if request.user|has_group:"gg" %}
# <p>User belongs to my group
# {% else %}
# <p>User doesn't belong to mygroup</p>
# {% endif %}    