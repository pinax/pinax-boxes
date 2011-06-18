from datetime import datetime

from django.db import models

from django.contrib.auth.models import User


class Box(models.Model):
    
    label = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    
    created_by = models.ForeignKey(User, related_name="boxes")
    last_updated_by = models.ForeignKey(User, related_name="updated_boxes")
    
    def __unicode__(self):
        return self.label
    
    class Meta:
        verbose_name_plural = "boxes"
    
    def save(self, **kwargs):
        super(Box, self).save(**kwargs)
        Revision.objects.create(
            box = self,
            label = self.label,
            content = self.content,
            orig_created_by = self.created_by,
            created_by = self.last_updated_by
        )


class Revision(models.Model):
    
    box = models.ForeignKey(Box, related_name="revisions")
    label = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    orig_created_by = models.ForeignKey(User, related_name="orig_revisions")
    
    created_on = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User, related_name="revisions")
    
    def __unicode__(self):
        return self.label
