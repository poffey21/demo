from __future__ import unicode_literals

from django.conf import settings
from django.db import models

class Message(models.Model):
    """ A basic message with a body and a user"""

    username = models.CharField(max_length=32)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']