from django.db import models
from django.utils import timezone


class Event(models.Model):
    #author = models.ForeignKey('auth.User')
    event_name = models.CharField(max_length=200)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    event_location = models.CharField(max_length=200)
    event_info = models.TextField()
    rockSoc_event = models.BooleanField(default=False)
    event_image = models.ImageField(upload_to='images/')
    link_to_Facebook_event = models.CharField(max_length=200, blank=True, null=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.event_name
