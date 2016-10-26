from __future__ import unicode_literals

from django.db import models

class Message(models.Model):
    """ A basic message with a body and a user"""

    username = models.CharField(max_length=32)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']