import datetime

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
