from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from .hooks import hookset


class Box(models.Model):

    label = models.CharField(max_length=100, db_index=True)
    content = models.TextField(blank=True)
    content_html = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name="boxes")
    last_updated_by = models.ForeignKey(User, related_name="updated_boxes")
    last_updated = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.content_html = hookset.parse_content(self.content)
        return super(Box, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "boxes"
