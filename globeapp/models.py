from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class SMPlatform(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class SMPost(models.Model):
    title = models.TextField(null=True, blank=True)
    location = models.ForeignKey(
        "Location",
        related_name="sm_posts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    language = models.ForeignKey(
        "Language",
        related_name="sm_posts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    brand = models.ForeignKey(
        "Brand",
        related_name="sm_posts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    body = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    post_author = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title or ""
