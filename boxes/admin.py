from django.contrib import admin

import reversion

from boxes.models import Box


class BoxAdmin(reversion.VersionAdmin):
    search_fields = ["content"]


admin.site.register(Box, BoxAdmin)
