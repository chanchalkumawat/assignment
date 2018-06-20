from __future__ import unicode_literals
import datetime
from django.db import models

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    date=models.DateField(default=datetime.date.today)
    city=models.CharField(max_length=250)





