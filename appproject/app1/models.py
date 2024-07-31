from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'{self.name}'


class Boost(models.Model):
    pass