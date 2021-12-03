from django.db import models
from django.utils.text import slugify


class TrainingPlan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    duration = models.PositiveSmallIntegerField(default=30)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TrainingPlan, self).save(*args, **kwargs)

