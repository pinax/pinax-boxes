from django.conf.urls import url

from .views import box_edit

urlpatterns = [
    url(r"^([-\w]+)/edit/$", box_edit, name="box_edit"),
]
