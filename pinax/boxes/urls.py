from django.conf.urls import url, patterns

from .views import box_edit


urlpatterns = patterns(
    "",
    url(r"^([-\w]+)/edit/$", box_edit, name="box_edit"),
)
