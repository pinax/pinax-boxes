"""
@@@ this is temporary until we have solved using AppConfig instead

    tracking: https://github.com/pinax/django-user-accounts/issues/184
"""
import importlib

from django.conf import settings  # noqa
from django.core.exceptions import ImproperlyConfigured

from appconf import AppConf


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = importlib.import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured(
            "Error importing {0}: '{1}'".format(module, e)
        )
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured(
            "Module '{0}' does not define a '{1}'".format(module, attr)
        )
    return attr


class PinaxBoxesAppConf(AppConf):

    HOOKSET = "pinax.boxes.hooks.DefaultHookSet"

    class Meta:
        prefix = "pinax_boxes"

    def configure_hookset(self, value):
        return load_path_attr(value)()
