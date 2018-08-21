from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings

from csclub.models import BaseModel


class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={'username': self.author.username, 'slug': self.slug})
