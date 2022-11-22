from django.db import models
from datetime import datetime
# Create your models here.


class Testresult(models.Model):
    id = models.IntegerField(primary_key=True)
    dateTime = models.DateTimeField(default=datetime.now())
    result = models.CharField(default="",max_length=30)