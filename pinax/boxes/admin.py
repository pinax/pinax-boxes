from django.contrib import admin

try:
    import reversion
    AdminBase = reversion.VersionAdmin
except ImportError:
    AdminBase = admin.ModelAdmin

from .models import Box


class BoxAdmin(AdminBase):
    list_display = ["label", "created_by", "last_updated_by", "last_updated"]
    search_fields = ["content"]


admin.site.register(Box, BoxAdmin)
