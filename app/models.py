from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    comp_date = models.DateTimeField('date completed',null=True, blank=True)
    def __str__(self):
        return self.task_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_completed_recently(self):
        return self.comp_date >= timezone.now() - datetime.timedelta(days=1)
