from django import template
from django.core.urlresolvers import reverse

from boxes.models import Box
from boxes.forms import BoxForm


register = template.Library()


@register.inclusion_tag("boxes/box.html", takes_context=True)
def box(context, label, show_edit=True, *args, **kwargs):
    
    request = context["request"]
    can_edit = request.user.has_perm("boxes.change_box")
    
    try:
        box = Box.objects.get(label=label)
    except Box.DoesNotExist:
        box = None
    
    if can_edit and show_edit:
        form = BoxForm(instance=box, prefix=label)
        form_action = reverse("box_edit", args=[label])
    else:
        form = None
        form_action = None
    
    return {
        "request": request,
        "label": label,
        "box": box,
        "form": form,
        "form_action": form_action,
    }
