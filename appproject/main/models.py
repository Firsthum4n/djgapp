from django.db import models
from django.urls import reverse


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    picture = models.ImageField(upload_to='images/')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    boost = models.ForeignKey('Boost', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Boost(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
