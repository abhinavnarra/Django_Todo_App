from django.db import models
from django.utils import timezone
import pytz
from datetime import datetime
from django.urls import reverse

class List(models.Model):
    list_name = models.CharField(max_length=250)
    due_date = models.DateTimeField()
    date_created = datetime.now()

    def get_absolute_url(self):
        return reverse('todo:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.list_name + str(self.date_created)
    # def __str__(self):
    #     return 'NAME  :' + self.list_name + '- DATE_CREATED   :' + str(self.date_created) +'- DUE_DATE  :' + str(self.due_date)

class Describe(models.Model):
    task = models.ForeignKey(List, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=1000)
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.task_description



