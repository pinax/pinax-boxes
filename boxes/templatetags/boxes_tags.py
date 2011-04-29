from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from boxes.models import Box


register = template.Library()


class BoxNode(template.Node):
    
    @classmethod
    def handle(cls, parser, token):
        bits = token.split_contents()
        return cls(bits[1])
    
    def __init__(self, label):
        self.label_var = template.Variable(label)
    
    def render(self, context):
        try:
            box = Box.objects.get(label=self.label_var.resolve(context))
        except Box.DoesNotExist:
            return u""
        return mark_safe(box.content.strip())


def box(parser, token):
    return BoxNode.handle_token(parser, token)
