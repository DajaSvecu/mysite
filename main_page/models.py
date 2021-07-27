from django.db import models

# Create your models here.

class Counter(models.Model):
    counter = models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.counter)
    