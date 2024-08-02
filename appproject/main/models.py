from django.db import models


class Heroes(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    picture = models.ImageField(upload_to='images/')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
