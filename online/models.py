from __future__ import unicode_literals
import datetime
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    account_time = models.DateTimeField('date published')