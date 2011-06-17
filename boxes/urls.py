from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("boxes.views",
    url(r"^(\d+)/edit/$", "box_edit", name="box_edit"),
)