import textile

from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from templatetag_sugar.register import tag
from templatetag_sugar.parser import Name, Variable, Constant, Optional, Model

from boxes.models import Box
from boxes.utils import sanitize_html

# TODO textile and sanitize_html are domain-specific to anime/gg
# rip them out and replace with generic filter hook

register = template.Library()

# TODO for a reusable app better to just bite the bullet and write this the
# long way and remove the templatetag-sugar dep
@tag(register, [Variable(), Optional([Variable()])])
def box(context, label, plain_html=False):
    try:
        box = Box.objects.get(label=label)
    except Box.DoesNotExist:
        return ""
    content = box.content.strip()
    if plain_html:
        return content
    return textile.textile(sanitize_html(content))
