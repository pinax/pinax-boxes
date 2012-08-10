import datetime

from django.http import HttpResponseForbidden
from django.shortcuts import redirect
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
        return redirect(next)
