from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from django.utils.timezone import now

Person = get_user_model()


class TreeInfo(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genus = models.CharField("Tree genus", max_length=255)
    more_info = models.TextField(
        "Additional information",
        default="No additional information given",
        max_length=255,
        blank=True,
    )
    files = models.FileField("Evidence", blank=True, null=True)


class Classification(models.Model):
    _class = models.CharField("Tree class", max_length=255)
    genus = models.CharField("Tree genus", max_length=255)
    species = models.CharField("Tree species", max_length=255)


class Notifications(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Notification title", max_length=255)

    status_choices = (("unread", "unread"), ("read", "read"))
    status = models.CharField(
        "Status", max_length=20, choices=status_choices, default="unread"
    )
    
    when = models.DateTimeField(default=now)
    
    time_sent = models.CharField("Time sent", max_length=150)

    def save(self, *args, **kwargs):
        val = timesince(self.when)
        if val:
            replacer = val.replace("hour", "hr")
            replacer = replacer.replace("minute", "min")
            setattr(self, "time_sent", f"{replacer} ago")

        super(Notifications, self).save(*args, **kwargs)


class Feedback(models.Model):
    name = models.CharField("Sender's name", max_length=255)
    email = models.EmailField("Your Email")
    subject = models.CharField("Subject", max_length=100)
    message = models.TextField("Message", max_length=255)
    date = models.DateField("Date sent", auto_now_add=True)
