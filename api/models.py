from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=160)
    publisher = models.CharField(max_length=60)

    def __str__(self):
        return self.name
