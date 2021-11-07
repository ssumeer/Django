from django.db import models
import datetime, jsonfield
# Create your models here.


class sensor(models.Model):
    servertime = models.DateTimeField(default=datetime.datetime.now(),blank=True)
    data = jsonfield.JSONField()

