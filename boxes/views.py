import datetime
import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from boxes.forms import BoxForm
from boxes.models import Box


@require_POST
def box_edit(request, label):
    
    if not request.user.has_perm("boxes.change_box"):
        return HttpResponseForbidden()
    
    next = request.GET.get("next")
    
    try:
        box = Box.objects.get(label=label)
    except Box.DoesNotExist:
        box = None
    
    form = BoxForm(request.POST, instance=box, prefix=label)
    
    if form.is_valid():
        if box is None:
            box = form.save(commit=False)
            box.label = label
            box.created_by = request.user
            box.last_updated_by = request.user
            box.last_updated = datetime.datetime.now()
            box.save()
        else:
            form.save()
        
        if request.is_ajax():
            data = {
                "html": render_to_string("boxes/box.html", {
                    "label": label,
                    "form": BoxForm(instance=box, prefix=label),
                    "box": box,
                    "form_action": reverse("box_edit", args=[label])
                }, context_instance=RequestContext(request))
            }
            return HttpResponse(json.dumps(data), mimetype="application/json")
        return redirect(next)
