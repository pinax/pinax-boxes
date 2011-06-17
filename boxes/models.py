from django.db import models


class Box(models.Model):
    
    label = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    
    def __unicode__(self):
        return self.label
    
    class Meta:
        verbose_name_plural = "boxes"

