from django.db import models

# Create your models here.
from applessons.models import Applessons


class Students(models.Model):
    name = models.CharField(max_length=50)
    surnames = models.CharField(max_length=100)
    identification_number = models.IntegerField()
    lessons = models.ForeignKey(
        Applessons,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.name
