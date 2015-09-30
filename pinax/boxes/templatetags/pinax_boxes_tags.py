from django import template
from django.core.urlresolvers import reverse

from ..forms import BoxForm
from ..models import Box


register = template.Library()


@register.inclusion_tag("pinax/boxes/_box.html", takes_context=True)
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

    context.update({
        "label": label,
        "box": box,
        "form": form,
        "form_action": form_action,
    })
    context.update(kwargs)
    return context
