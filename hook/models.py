from django.db import models
from django.utils import timezone

# from django_hstore import hstore

# Create your models here.

class paystackreceive(models.Model):
    received_at = models.DateTimeField(help_text="When we received the event.")
    payload = models.JSONField(default=None, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["received_at"]),
        ]
    def __str__(self):
        return self.received_at