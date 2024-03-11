from django.db import models

from django.db import models


class MessageEvent(models.Model):
   
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    def __str__(self):
        return f'Reminder at {self.date} {self.time}'
