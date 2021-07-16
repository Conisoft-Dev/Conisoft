from django.db import models

# Create your models here.

class Worshop(models.Model):
    name = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.DateTimeField()
    open_slots = models.IntegerField()
    taken_slots = models.IntegerField(default=0)
    zoom_link = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name