from django.db import models


class Trial(models.Model):
    email = models.CharField(max_length=200, blank=False, default='')
    event_id = models.CharField(max_length=200,blank=False, default='')
    summary = models.CharField(max_length=200,blank=False, default='')
    start_dateTime = models.CharField(max_length=200,blank=False, default='')
    end_dateTime = models.CharField(max_length=200,blank=False, default='')
    attendee_email = models.CharField(max_length=3000,blank=False, default='')
    location = models.CharField(max_length=200,blank=False, default='')
    creator_email = models.CharField(max_length=200,blank=False, default='')
    organizer_email = models.CharField(max_length=200,blank=False, default='')
    recurrence = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
