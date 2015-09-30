from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import permission_required

from .forms import BoxForm
from .models import Box


@require_POST
@permission_required("boxes.change_box", raise_exception=True)
def box_edit(request, label):
    box, _ = Box.objects.get_or_create(label=label, defaults={
        "created_by": request.user,
        "last_updated_by": request.user
    })
    form = BoxForm(request.POST, instance=box, prefix=label)

    if not form.is_valid():
        return HttpResponseBadRequest()  # not sure how this will ever happen

    box = form.save(commit=False)
    box.last_updated_by = request.user
    box.last_updated = timezone.now()
    box.save()

    if not request.is_ajax():
        return redirect(
            request.POST.get("next", request.GET.get("next", request.path))
        )

    data = {
        "html": render_to_string("boxes/_box_body.html", {
            "label": label,
            "form": BoxForm(instance=box, prefix=label),
            "box": box,
            "form_action": reverse("box_edit", args=[label]),
            "saved": True
        }, context_instance=RequestContext(request))
    }
    return JsonResponse(data)
