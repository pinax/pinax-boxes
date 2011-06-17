from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module


def _can_edit(*args, **kwargs):
    """
    This is meant to be overridden in your project per domain specific
    requirements.
    """
    return True


def get_can_edit():
    import_path = getattr(settings, "BOXES_CAN_EDIT_CALLABLE", None)
    if import_path is None:
        return _can_edit
    
    try:
        dot = import_path.rindex(".")
    except ValueError:
        raise ImproperlyConfigured("%s isn't a Python path." % import_path)
    
    module, func = import_path[:dot], import_path[dot + 1:]
    
    try:
        mod = import_module(module)
    except ImportError, e:
        raise ImproperlyConfigured("Error importing module %s: '%s'" %
                                   (module, e))
    
    try:
        return getattr(mod, func)
    except AttributeError:
        raise ImproperlyConfigured("Module '%s' does not define a '%s' "
                                   "class." % (module, func))


can_edit = get_can_edit()