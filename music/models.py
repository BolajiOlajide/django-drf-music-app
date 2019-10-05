from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.title} - {self.artist}"
