from django.db import models
from autoslug import AutoSlugField


def my_slug_func(title):
    title_x = str((title.replace(' ', '_')))
    title_z = title_x.lower()
    return title_z


class Post(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title',
                         unique_with=['creation_date'],
                         slugify=my_slug_func)

    def __str__(self):
        return self.title
