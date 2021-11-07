from django.db import models
import datetime, jsonfield
# Create your models here.


class sensor(models.Model):
    when = models.DateTimeField(default=datetime.datetime.now(),blank=True)
    data = jsonfield.JSONField()
