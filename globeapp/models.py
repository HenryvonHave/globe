from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Brands(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=True, blank=True)


class SMPost(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=True, blank=True)
    location = models.ForeignKey(
        "Location",
        related_name="location",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
