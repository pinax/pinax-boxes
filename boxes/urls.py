from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("boxes.views",
    url(r"^([-\w]+)/edit/$", "box_edit", name="box_edit"),
)
