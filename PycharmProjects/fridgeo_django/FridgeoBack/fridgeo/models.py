import email_validator
from django.db import models
from django.urls import reverse
from . import views


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=20, null=False)


class Receipt(models.Model):
    title = models.CharField(max_length=255)
    receipt = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
