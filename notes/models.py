from django.db import models

from csclub.models import BaseModel


class Note(BaseModel):
    title = models.CharField(max_length=120)
    description = models.TextField()
    file_url = models.URLField()
    download_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
