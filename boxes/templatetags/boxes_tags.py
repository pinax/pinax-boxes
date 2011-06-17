from django import template
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_str
from django.utils.translation import ugettext_lazy as _
from django.template.defaulttags import kwarg_re

from boxes.models import Box
from boxes.authorization import can_edit


register = template.Library()


class BoxNode(template.Node):
    
    @classmethod
    def handle(cls, parser, token):
        bits = token.split_contents()
        if len(bits) < 2:
            raise template.TemplateSyntaxError("'box' takes at least one argument "
                                               " (label of the content to display)")
        args = []
        kwargs = {}
        label = parser.compile_filter(bits[1])
        bits = bits[2:]
        if len(bits):
            for bit in bits:
                match = kwarg_re.match(bit)
                if not match:
                    raise template.TemplateSyntaxError("Malformed arguments to 'box' tag")
                name, value = match.groups()
                if name:
                    kwargs[name] = parser.compile_filter(value)
                else:
                    args.append(parser.compile_filter(value))
        return cls(label, args, kwargs)
    
    def __init__(self, label, args, kwargs):
        self.label = label
        self.args = args
        self.kwargs = kwargs
    
    def render(self, context):
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict([(smart_str(k, "ascii"), v.resolve(context))
                        for k, v in self.kwargs.items()])
        show_edit_link = can_edit(*args, **kwargs)
        
        box, created = Box.objects.get_or_create(
            label=self.label
        )
        
        content = box.content.strip()
        
        if len(content) == 0:
            content = _("<p>No content for this box has been created yet.</p>")
        
        if show_edit_link:
            url = reverse("box_edit", args=[box.pk])
            content += " <a href=\"%s\" class=\"boxes-edit-link\" rel=\"facebox\">%s</a>" % (url, unicode(_("Edit")))
        
        return mark_safe(content)


@register.tag
def box(parser, token):
    """
    {% box label [args] [kwargs] %}
    
    All args/kwargs are passed directly to callable defined in the setting
    BOXES_CAN_EDIT_CALLABLE which returns True or False to determine if the
    box can be edited.
    """
    return BoxNode.handle(parser, token)
