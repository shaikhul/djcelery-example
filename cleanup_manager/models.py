import datetime
from django.utils import timezone

from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
    	#RuntimeWarning: SQLite received a naive datetime while time zone support is active
    	#use tzinfo as follows
        return self.created_at >= datetime.datetime.utcnow().replace(tzinfo=timezone.utc) - datetime.timedelta(minutes=30)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)