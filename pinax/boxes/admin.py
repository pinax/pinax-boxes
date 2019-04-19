from django.contrib import admin

from .models import Box

try:
    from reversion.admin import VersionAdmin as AdminBase
except ImportError:
    AdminBase = admin.ModelAdmin


class BoxAdmin(AdminBase):
    list_display = ["label", "created_by", "last_updated_by", "last_updated"]
    search_fields = ["content"]


admin.site.register(Box, BoxAdmin)
