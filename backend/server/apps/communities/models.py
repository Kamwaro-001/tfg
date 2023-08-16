import string, secrets

from django.db import models

def verification_code():
    return "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8)
    )


class Community(models.Model):
    name = models.CharField("Community name", max_length=255)
    region = models.CharField("Region", max_length=255)
    created_by = models.CharField("Created by", max_length=255)
    verif_code = models.CharField("Verification code", max_length=9, unique=True)

    visibility_choices = (("private", "private"), ("public", "public"))
    visibility = models.CharField(
        "Visibility", max_length=20, choices=visibility_choices, default="private"
    )

    description = models.TextField("Community description")
    date_created = models.DateField("Created on", auto_now_add=True)

    def save(self, *args, **kwargs):
        setattr(self, 'verif_code', verification_code())
        CommunityMembers.objects.create(
            community=getattr(self, "name"), username=getattr(self, "created_by")
        )
        super(Community, self).save(*args, **kwargs)


class CommunityMembers(models.Model):
    community = models.CharField("Member to", max_length=255)
    username = models.CharField("Member username", max_length=255)
    date_joined = models.DateField("Joining date", auto_now_add=True)


class CommunityActivities(models.Model):
    community = models.CharField("Community", max_length=255)
    title = models.CharField("Activity title", max_length=255)
    description = models.TextField("Activity description")
    planned_date = models.DateField("Planned date", blank=True)

    status_choices = (
        ("PL", "planned"),
        ("OG", "ongoing"),
        ("Co", "completed"),
        ("Ca", "cancelled"),
    )
    status = models.CharField(
        "Activity status", max_length=20, choices=status_choices, default="planned"
    )

    summary = models.TextField("End of activity summary", blank=True)
