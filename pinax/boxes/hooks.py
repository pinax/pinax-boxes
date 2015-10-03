class DefaultHookSet(object):

    def parse_content(self, content):
        return content


class HookProxy(object):

    def __getattr__(self, attr):
        from .conf import settings  # if put globally there is a race condition
        return getattr(settings.PINAX_BOXES_HOOKSET, attr)


hookset = HookProxy()
