from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(models.Model):

    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return "todo : {}" .format(self.name)
