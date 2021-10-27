from django.db import models
from django.utils import timezone

# from django_hstore import hstore

# Create your models here.

class hooktransaction(models.Model):
    UNPROCESSED = 1
    PROCESSED = 2
    ERROR = 3

    STATUSES = (
        ()
    )