from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from boxes.forms import BoxEditForm
from boxes.models import Box


# @@@ put privilege checks around this using a boxes.check_permissions function
def box_edit(request, pk):
    box = get_object_or_404(Box, pk=pk)
    if request.method == "POST":
        form = BoxEditForm(request.POST, instance=box)
        if form.is_valid():
            form.save()
            return render_to_response("boxes/refresh.html", {})
    else:
        form = BoxEditForm(instance=box)
    ctx = {
        "form": form,
        "box": box,
    }
    ctx = RequestContext(request, ctx)
    return render_to_response("boxes/box_edit.html", ctx)

